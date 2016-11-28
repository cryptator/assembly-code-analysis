#!/usr/bin python2
import os
import sys
import shutil

print "Enter folder to list all unique files: (Ex: /home/user/files)"
folderLoc= raw_input("Enter file location: ")


if not os.path.exists(folderLoc):
	print "Folder doesn't exist"
	sys.exit()

folderLoc2=folderLoc+'/duplicate_files'
if not os.path.exists(folderLoc2):
	os.system("mkdir \""+ folderLoc2+"\"")

os.system("find -name '*.ASM' -print0 | xargs -0 md5sum | sort | uniq -Dw 32 > unique1.txt")
os.system("find -name '*.asm' -print0 | xargs -0 md5sum | sort | uniq -Dw 32 > unique2.txt")

with open("unique1.txt") as f1:
	arr=[]
	for line in f1:
		a=line.split()
		if a[0] not in arr:
			arr.append(a[0])

		else:
			fname= a[1][2:]
			source=folderLoc+ "/"+fname
			destination=folderLoc+ "/duplicate_files"
			shutil.move(source, destination)

with open("unique2.txt") as f1:
	arr=[]
	for line in f1:
		a=line.split()
		if a[0] not in arr:
			arr.append(a[0])

		else:
			fname= a[1][2:]
			source=folderLoc+ "/"+fname
			destination=folderLoc+ "/duplicate_files"
			shutil.move(source, destination)

os.remove("unique1.txt")
os.remove("unique2.txt")
