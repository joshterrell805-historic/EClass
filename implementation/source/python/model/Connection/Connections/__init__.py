# This is the Connection that all other Connections inherit from.
# No one in EClass should ever use one of these directly.. Connections are only
# used by Connection.
from twisted.internet.protocol import Factory, Protocol, ClientFactory
from twisted.internet import reactor
import pickle
from threading import Thread

# Client, Server, and BaseConnection are all that should be used outside of this
# module

class BaseConnection(object):
   """
   Send and receive objects over the network. One of these Connections is
   returned from Sever and Client in the callbacks when a new connection
   has been made.
   """
   def send(self, message):
      self.__protocol.transmit(message)

   def setProtocol(self, protocol):
      self.__protocol = protocol

   def getRemote(self):
      return self.__protocol.transport.getPeer()

   def close(self):
      """
      Close this connection.
      """
      self.__protocol.loseConnection()

   def onMessage(self, message):
      """
      Callback called whenever an object is received.
      This should be overriden.
      @param message: the object recieved by the person at the other side.
      """
      pass

   def onClose(self, reason):
      """
      Callback called whenever the connection is closed.
      This should be overriden.
      @param reason: the reason this connection was closed.
      """
      pass

class BaseProtocol(Protocol):
   def __init__(self, onConnection, baseConnection):
      self.__onConnection = onConnection
      self.__baseConnection = baseConnection

   def connectionMade(self):
      print('connection success')
      if self.__onConnection:
         self.__onConnection(self.__baseConnection)

   def connectionLost(self, reason):
      self.__baseConnection.onClose(reason)

   def connectionFailed(self, reason):
      self.__baseConnection.onClose(reason)

   def dataReceived(self, data):
      message = pickle.loads(data)
      self.__baseConnection.onMessage(message)

   def loseConnection(self):
      self.transport.loseConnection()

   def transmit(self, message):
      data = pickle.dumps(message)
      self.transport.write(data)

class ServerConnectionFactory(Factory):
   def __init__(self, ConnectionClass, onConnection):
      #called in protocol.connectionMade
      self.__ConnectionClass = ConnectionClass
      self.__onConnection = onConnection

   def buildProtocol(self, addr):
      connection = self.__ConnectionClass()
      protocolInstance = BaseProtocol(self.__onConnection, connection)
      connection.setProtocol(protocolInstance)
      return protocolInstance

class ClientConnectionFactory(ClientFactory):
   def __init__(self, ConnectionClass, onConnection, onConnectionFailed):
      #called in protocol.connectionMade
      self.__ConnectionClass = ConnectionClass
      self.__onConnection = onConnection
      self.__onConnectionFailed = onConnectionFailed

   def buildProtocol(self, addr):
      connection = self.__ConnectionClass()
      protocolInstance = BaseProtocol(self.__onConnection, connection)
      connection.setProtocol(protocolInstance)
      return protocolInstance

   def clientConnectionFailed(self, connection, reason):
      self.__onConnectionFailed(reason)
      
def startReactorIfNotStarted():
   # http://stackoverflow.com/questions/14274916/execute-twisted-reactor-run-in-a-thread
   # only call reactor inside reactor's thread. fuck.
   if not reactor.running:
      Thread(target=reactor.run, args=(False,)).start()
   
class Server(object):
   __singleThread = False
   @staticmethod
   def listen(port, ConnectionClass, onListen, onConnection):
      listeningPort = reactor.listenTCP(port,
         ServerConnectionFactory(ConnectionClass, onConnection)
      )
      print('listening on ' + str(listeningPort.getHost().port))
      onListen(listeningPort)
      if Server.__singleThread and not reactor.running:
         reactor.run()
      else:
         startReactorIfNotStarted()

   @staticmethod
   def singleThread():
      # call this method to make the listen happen on the same thread
      Server.__singleThread = True

class Client(object):
   @staticmethod
   def connect(hostname, port, ConnectionClass, onConnection, onConnectFail):
      print('connecting to ' + hostname + ':' + str(port))
      def failWrap(reason):
         onConnectFail()

      reactor.connectTCP(hostname, port,
         ClientConnectionFactory(ConnectionClass, onConnection, failWrap),
         3
      )
      startReactorIfNotStarted()

