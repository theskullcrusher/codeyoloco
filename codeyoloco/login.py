"""
__author__:surajshah
"""

from ictf import iCTF
import os, sys
import ConfigParser

def main():
	try:
		configParser = ConfigParser.RawConfigParser()   
		configParser.read("codeyoloco/config.txt")

		team_ip = 'http://' + str(configParser.get("login","team-ip")) + '/'
		i = iCTF(team_ip)

		t = i.login(str(configParser.get("login","username")),
			str(configParser.get("login","password")))
		key_info = t.get_ssh_keys()

		with open("root_key", 'w+') as f:
			f.write(key_info['root_key'])
		os.chmod("root_key", 0600)

		with open("ctf_key", 'w+') as f:
			f.write(key_info['ctf_key'])
		os.chmod("ctf_key", 0600)

		ssh_script = """
		#!/bin/bash
		ssh -i {} -p {} {}@{} -o IdentitiesOnly=yes
		"""

		with open("root_ssh.sh", 'w+') as f:
			ssh_root = ssh_script.format("./root_key", key_info['port'], 'root', key_info['ip'])
			f.write(ssh_root)
		os.chmod("root_ssh.sh", 0700)

		with open("ctf_ssh.sh", 'w+') as f:
			ssh_ctf = ssh_script.format("./ctf_key", key_info['port'], 'root', key_info['ip'])
			f.write(ssh_ctf)
		os.chmod("ctf_ssh.sh", 0700)

		print 'Team ID: {}'.format(key_info['team_id'])
		print 'IP Address: {}'.format(key_info['ip'])
		print 'Port: {}'.format(key_info['port'])
		print 'Connect to root with: ./root_ssh.sh'
		print 'Connect to ctf with: ./ctf_ssh.sh'


	except Exception as e:
		exc_type, exc_obj, exc_tb = sys.exc_info()
		fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
		print(e, exc_type, fname, exc_tb.tb_lineno)


if __name__ == '__main__':
	main()