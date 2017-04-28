#!/usr/bin/python
__author__ = "Laurence Chang and Josh Smith"

#Program to find the most recently updated flag in /opt/ctf/<servicefile>/rw/
#This can be done by performing the command ls 

import os, time


#using OS due to subprocess shell escaping strings. We want to be able to manipulate variables i think
def main():
	#ls -t | head -n1
	var = "/home/laurence/test/"	# we should somehow be able to dynamically change this variable maybe?
	fileToCat = os.popen("ls -t " + var + " | head -n1").read()	
	#print fileToCat
	payload = os.popen("cat " + var + fileToCat).read()
	print payload
	
'''To do thoughts '''
# Construct http packet using payload
# Send http packet to our hostname
# maybe optimize somehow such as checking if var != prevVar rather than relying soley on time?





	
	

if __name__ == "__main__":
	while(1):
		main()
		time.sleep(10)
    	


