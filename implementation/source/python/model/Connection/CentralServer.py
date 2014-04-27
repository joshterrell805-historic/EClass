# run this file directly to start the central server

import os, json, signal, sys, time
from threading import Thread
from twisted.internet import reactor
from Connections import Server
from Connections.CentralServer_ServerOf_User import CentralServer_ServerOf_User as CentralServer

configFile = open(os.path.dirname(__file__) + '/config.json')
settings = json.load(configFile)['central server']

def onConnect(connection):
   pass
def onFail(reason):
   print('Failed to start the central server')
   print(reason)


Server.listen(settings['port'], CentralServer, onConnect, onFail)
