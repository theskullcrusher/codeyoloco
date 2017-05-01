#!/usr/bin/python

import sys, os

fFound = False
hFound = False
bFound = False
boFound = False
poFound = False
cFound = False
dFound = False
hidFound = False
owner = ""
file_name = ""
args = []

# This creates backups of a file automatically
def backup(f,hid):
	readddot = False
	# PRINTS A MESSAGE SO YOU KNOW THE OPTIONS CHOSEN
	print "We are backing up " + f,
	if hid:
		print "in a hidden format"
	else:
		print ""
	# CREATING NAMES
	if f[0] == ".":
		readddot = True
		f = f[1:]
	fp = f.split(".")
	f2 = ""
	for fp2 in fp[1:]:
		f2 = f2+"."+fp2
	backup_name = fp[0]+"_backup"+f2
	patch_name = fp[0]+"_patched"+f2
	if readddot:
		backup_name = "."+backup_name
		patch_name = "."+patch_name
	if hid:
		backup_name = "."+backup_name
		patch_name = "."+patch_name
	print backup_name+"\n"+patch_name
	
	# SET UP COMMAND
	boCommand = ""
	boChown = ""
	poCommand = ""
	poChown = ""
	command = ""
	
	boCommand = "cp "+f+" "+backup_name
	boChown = "chown "+owner+" "+backup_name
	poCommand = "cp "+f+" "+patch_name
	poChown = "chown "+owner+" "+patch_name
	if boFound:
		if cFound:
			boCommand = boCommand+" && "+boChown
		command = boCommand
	elif poFound:
		if cFound:
			poCommand = poCommand+" && "+poChown
		command = poCommand
	else:
		command = boCommand+" && "+poCommand
		if cFound:
			command = command+" && "+boChown+" && "+poChown
	
	print "\n\nThe COMMAND is:"
	print command
	
	os.system(command)
# This deletes backups of a file automatically
def delete_backup(f,hid):
	readddot = False
	# PRINTS A MESSAGE SO YOU KNOW THE OPTIONS CHOSEN
	print "We are deleting",
	if hid:
		print "hidden",
	print "backups of " + f
	
	# CREATING NAMES
	if f[0] == ".":
		readddot = True
		f = f[1:]
	fp = f.split(".")
	f2 = ""
	for fp2 in fp[1:]:
		f2 = f2+"."+fp2
	backup_name = fp[0]+"_backup"+f2
	patch_name = fp[0]+"_patched"+f2
	if readddot:
		backup_name = "."+backup_name
		patch_name = "."+patch_name
	if hid:
		backup_name = "."+backup_name
		patch_name = "."+patch_name
	print backup_name+"\n"+patch_name
	
	# SET UP COMMAND
	command = ""
	if boFound:
		command = "rm ./"+backup_name
	elif poFound:
		command = "rm ./"+patch_name
	else:
		command= "rm ./"+patch_name+" ./"+backup_name
	
	print "\n\nThe COMMAND is:"
	print command
	
	os.system(command)
# This prints the options for command line use
def printBackupOptions():
	print "\n\nThe input is ./backup.py -f <filename> [-h] " +\
	      "[-b] [-bo] [-po] [-c <owner>] [-d] [--hidden]\n" +\
	      "Choose EITHER -b or -d\n" +\
	      "-f specifies the what file needs to be backed up\n" +\
	      "-h prints the help for this file\n" +\
	      "-b backs up the specified file (default)\n" +\
	      "-bo does the backup only and not the patch file\n" +\
	      "-po does the patch only and not the backup file\n" +\
	      "-c specifies the new owners of the file\n" +\
	      "\towner = [user][:usergroup]\n" +\
	      "-d deletes backups of the specified file\n" +\
	      "--hidden adds a \".\" to the front so ls -a or la are needed to find them\n\n"

# This looks threw the options given on the command line
def findVars(args,f):
	global fFound, hFound, bFound, boFound, poFound, cFound, dFound, hidFound, file_name, owner
	fF = False
	hF = False
	bF = False
	boF = False
	poF = False
	cF = False
	dF = False
	hidF = False
	for i in range(args.__len__()):
		if args[i] == "-f":
			if f:
				"-f is duplicated"
				sys.exit()
			fF = True
			f = True
			try:
				if not findVars(args[i+1],True):
					file_name = args[i+1]
				else:
					print "Choose a file to backup\n"
					sys.exit()
			except:
				print "Choose a file to backup\n"
				sys.exit()
		elif args[i] == "-h":
			hF = True
		elif args[i] == "-b":
			bF = True
		elif args[i] == "-bo":
			boF = True
		elif args[i] == "-po":
			poF = True
		elif args[i] == "-d":
			dF = True
		elif args[i] == "--hidden":
			hidF = True
		elif args[i] == "-c":
			try:
				print args[i+1]
				if not findVars(args[i+1],True):
					owner = args[i+1]
					cF = True
			except:
				print "Choose a user to give ownership"
			if not cF:
				print "Choose a user to give ownership"
				print "For now we will run as if no -c was given"
		else:
			if args[i][0] == "-":
				print "\nCommand " + args[i] + " not found"
	fFound = fF
	hFound = hF
	bFound = bF
	boFound = boF
	poFound = poF
	cFound = cF
	dFound = dF
	hidFound = hidF
	if fF or hF or bF or boF or poF or cF or dF or hidF:
		return True
	return False


# This is for command line use
if __name__ == "__main__":
	# Finding arguments
	args = sys.argv
	args_len = args.__len__()
	if args_len == 1:
		printBackupOptions()
		sys.exit()
	findVars(args,False)
	
	# Printing required messages
	if hFound:
		printBackupOptions()
	if not fFound:
		print "Choose a file to backup\n"
		sys.exit()
	if bFound and dFound:
		print "Choose EITHER -b or -d\n"
		sys.exit()
	if cFound:
		print "You might need to rerun with root permissions\n"
	if boFound and poFound:
		print "Both \"-bo\" and \"-po\" were found. Treating as if neither were input"
		boFound = False
		poFound = False
	
	# Actual code to do stuff
	# Use the below functions if calling from another script
	if dFound:
		delete_backup(file_name,hidFound)
	else:
		backup(file_name,hidFound)
