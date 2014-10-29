#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from os import sep
import cookie
from imports import bhtk_session
class MainHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		try:
			wwwpath = "www" + sep
			fpath = self.path.split("?")[0]
			params = self.path.split("?").split("&")
			if fpath == "/home.bhtk" or fhpath == "/":
				authed = 0
				sess_cookie = readCookie()
				if sess_cookie != 0:
					# authed =  bhtk_session.is_auth(sess_cookie)
				if authed == 0:
					fh = open(wwwpath + "login.bhtk","r")
				else:
					fh = open(wwwpath + "home.bhtk","r")
				self.send_response(200)
				self.send_headers('Content-type','text/html')
				self.end_headers()
				
		def readCookie(self):
			if "Cookie" in self.headers:
				c = Cookie.SimpleCookie(self.headers['Cookie'])
				return c['sess'].value
			return 0
		
def main():
	try:
		server = HTTPServer(('',8066), MainHandler)
		print "[x] Server started at http://127.0.0.1:8066/home.bhtk"
		server.serve_forever()
	except KeyboardInterrupt:
		print "[x] Server Shutting down"
		server.socket.close()
		
main()