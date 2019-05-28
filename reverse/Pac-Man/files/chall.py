#!/usr/bin/env python2

import SocketServer
import subprocess

SocketServer.TCPServer.allow_reuse_address = True

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		subprocess.call(["python","main.py"])

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
	pass

if __name__ == '__main__':
	server = ThreadedTCPServer(('0.0.0.0', 2000), ThreadedTCPRequestHandler)
	server.allow_reuse_address = True
	server.serve_forever()