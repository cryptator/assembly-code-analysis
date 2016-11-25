#!/usr/bin python2

import os
import sys
import argparse
import shutil

parser = argparse.ArgumentParser(description='Use objdump to scan specfied folder for .exe files and dissamble them, i.e. convert to .asm files.')
parser.add_argument('-d','--directory', help='Location of Folder to scan for .exe files Ex. /home/user/malwares/EXE', required=True)
args = vars(parser.parse_args())

folderLoc=args['directory']

if not os.path.exists(folderLoc):
	print "Directory doesn't exist"
	sys.exit()


folderLoc2=folderLoc+'/objdump_error'
if not os.path.exists(folderLoc2):
	os.system("mkdir \""+ folderLoc2+"\"")

folderLoc3=folderLoc+'/assembly_codes'
if not os.path.exists(folderLoc3):
	os.system("mkdir \""+ folderLoc3+"\"")

files=[]
for file in os.listdir(folderLoc):
    if file.endswith(".exe"):
    	files.append(file)
    if file.endswith(".EXE"):
    	files.append(file)


for file in files:
	source = folderLoc+'/'+file
	dest=folderLoc3+'/'+file
	# os.system("objdump -d \"" + file + "\"> \"" + file + ".asm\"")
	test="objdump -d \"" + source + "\" 2> error_file > \"" + dest + ".asm\""
	# print test
	os.system(test)
	# os.system("objdump -d \"" + file + "\" 2> error_file > \"" + file + ".asm\"")
	
	f1=open('error_file','r')
	a=f1.readline()
	if a:
		b=a.split()
		# print b
		if b[0]=="objdump:":
			tempfile1=dest+".asm"
			os.remove(tempfile1)
			# os.system("rm " + dest + ".asm")
			destination = folderLoc2+'/'
			# print source,destination
			shutil.move(source, destination)
	f1.close()

# os.system("rm error_file")
os.remove("error_file")
