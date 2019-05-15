#!/usr/bin/env python2

import SocketServer

flag = open('flag.txt').read().strip()

SocketServer.TCPServer.allow_reuse_address = True


class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		self.request.settimeout(15)
		self.request.sendall("Password: \n")

		x = self.request.recv(2048)
		x = x.lower().strip('\n').replace(' ','')
		try:
			if x == "insecurekeithwasanenigma":
				self.request.sendall("\nHere is your flag!\n")
				self.request.sendall(flag+"\n")
			else:
				self.request.sendall("\nNo...\n\n")
				return
		except Exception:
			ret = 'Error'

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
	pass

if __name__ == '__main__':
	server = ThreadedTCPServer(('0.0.0.0', 2000), ThreadedTCPRequestHandler)
	server.allow_reuse_address = True
	server.serve_forever()