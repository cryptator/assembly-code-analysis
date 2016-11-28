#!/usr/bin python2

import os
import sys
import argparse

'''
opcodeList.txt contains the list of opcodes that we have to scan.
We save all the opcodes in a list.
'''

f1 = open('opcodeList.txt', 'r')
opcodes=[]
opcodes.append('FileName')						
for eachLine in f1:
	opcodes.extend(eachLine.split())
f1.close()

num_opcodes=len(opcodes)-1
# As we added Filename Paramater on our own, we subtract one.

# Argument Parser
parser = argparse.ArgumentParser(description='Output a csv file containing the frequency of all opcodes for each .asm file in the specified directory.')
parser.add_argument('-d','--directory', help='Location of Directory(folder) to scan for .asm files', required=True)
parser.add_argument('-o','--outfile', help='Name of the output .csv file', required=True)
args = vars(parser.parse_args())

folderLoc=args['directory']
out_file=args['outfile']

# Checking if the user entered directory exists or not.
if not os.path.exists(folderLoc):
	print "Directory doesn't exist"
	sys.exit()

'''
Scanning the entered folder for .ASM files and 
adding their names in a list
'''

files=[]
for file in os.listdir(folderLoc):
    if file.endswith(".ASM"):
    	files.append(file)
    if file.endswith(".asm"):
    	files.append(file)


# Checking if the folder contains no .ASM files.
if len(files)==0:
	print "No .ASM or .asm files exist in folder specified"
	sys.exit()

# Output file
outfile= open('%s' % out_file, 'w')


#FirstLine --> Has Filename and the index of opcode in the opcodeList
firstLine=[]
firstLine.append('FileName')
for i in range(1,num_opcodes+1):
	firstLine.append(i)
outfile.write( ",".join(str(x) for x in firstLine))
outfile.write("\n")

'''
*	number is a list that is going to save the frequency of each opcode.
	We initialize it to 0, with its first element saving the filename
	on which the loop is working. (See output format)
*	First we check if the list is not empty(empty line).
*	We split eachline and save it to a list.
*	Then we scan the first word, as the first word only contains the opcode.
*	We check if the that word starts with ";" : indicating a comment or
	ends with ":" : indicating a function , for both cases there is no need
	to work further on that word.
*	If all the above conditions fail, we search for that word in the opcode list,
	if it is present, we increment the corresponding counter by one and then continue with the next line
*	For each file we print the frequency for with each opcode occurs, separated by comma (.csv format)
*	Loop for all .ASM files 

'''
for file in files:
	f1 = open(os.path.join(folderLoc, file), 'r')
	number=[0]*(num_opcodes+1)
	number[0]='%s' % file
	for line in f1:
		splitter = line.split()
		if splitter:
			a=splitter[0]
			if not(a.startswith(';') or a.endswith(':')):
				if a in opcodes:
					number[opcodes.index(a)]+=1

	outfile.write( ",".join(str(x) for x in number))
	outfile.write("\n")
	f1.close()

outfile.close()