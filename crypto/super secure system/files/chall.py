#!/usr/bin/env python2

import SocketServer
from random import choice
import string
import binascii

flag = open('flag.txt').read().strip()
char_set = string.ascii_uppercase + string.ascii_lowercase + string.digits

def gen_key():
	return "".join(choice(string.printable) for _ in char_set)

def encrypt(str1, key):
	return "".join(chr(ord(i) ^ ord(j)) for (i, j) in zip(str1, key))

SocketServer.TCPServer.allow_reuse_address = True

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		self.request.settimeout(15)
		self.request.sendall("* * * SUPER SECURE SYSTEM * * *\n")
		self.request.sendall("My encryption system is impossible to crack if used once!\n")
		self.request.sendall("You can use this system to encrypt any of your messages with my super special key!!!\n")
		key = gen_key()
		self.request.sendall("Here is my super secret message: {}\n\n".format(binascii.hexlify(encrypt(flag,key).encode('utf8'))))

		while True:
			self.request.sendall("Enter the message you want to encrypt: ")
			try:
				x = self.request.recv(2048)
				x = x.strip('\n')
				try:
					self.request.sendall("\nEncrypted: {}\n\n".format(binascii.hexlify(encrypt(x,key).encode('utf8'))))
				except Exception:
					ret = 'Error'
			except:
				self.request.sendall("\n\nTime out!")
				return

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
	pass

if __name__ == '__main__':
	server = ThreadedTCPServer(('0.0.0.0', 2000), ThreadedTCPRequestHandler)
	server.allow_reuse_address = True
	server.serve_forever()