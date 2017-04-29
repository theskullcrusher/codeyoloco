#!/usr/bin/python
__author__ = "Laurence Chang and Josh Smith"

#Program to find the most recently updated flag in /opt/ctf/<servicefile>/rw/
#This can be done by performing the command ls 

import os, subprocess, time


#using OS due to subprocess shell escaping strings. We want to be able to manipulate variables i think
def main():	
	#ls -t | head -n1
	var = "/opt/ctf/sample_py/rw/"	# we should somehow be able to dynamically change this variable maybe?	
	p1 = subprocess.Popen(["ls", "-t", var], stdout=subprocess.PIPE)
	p2 = subprocess.Popen(["head", "-n1"], stdin=p1.stdout, stdout=subprocess.PIPE)
	output = p2.stdout.read()
#	print output

	cmd = "cat " + var + output
#	print cmd
	flag = os.popen(cmd).read()
	print flag	

	

	
'''To do thoughts '''
# Construct http packet using payload
# Send http packet to our hostname
# maybe optimize somehow such as checking if var != prevVar rather than relying soley on time?



if __name__ == "__main__":
	while(1):
		main()
		time.sleep(5)
    	


