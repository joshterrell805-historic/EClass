# run this file directly to start the central server

import os, json, signal, sys, time
from threading import Thread
from twisted.internet import reactor
from Connections import Server
from Connections.CentralServer_ServerOf_User import CentralServer_ServerOf_User as CentralServer

configFile = open(os.path.dirname(__file__) + '/config.json')
settings = json.load(configFile)['central server']

def onListen(port):
   pass

Server.singleThread()
Server.listen(settings['port'], CentralServer, onListen, None)
