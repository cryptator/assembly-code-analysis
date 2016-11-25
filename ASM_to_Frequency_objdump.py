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

# Checking if the variable is a valid hexadecimal
def CheckHex(var):
    try:
        Hex=int(var, 16)
        return True
    except ValueError: 
        return False

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
outfile.write(",".join(str(x) for x in firstLine))
outfile.write("\n")


'''
*	number is a list that is going to save the frequency of each opcode.
	We initialize it to 0, with its first element saving the filename
	on which the loop is working. (See output format)
*	First we check if the list is not empty(empty line).
*	We split eachline and save it to a list.
*	Then we check if its length is less that 2,
	indicating that there are no opcodes in that line.
	Ex:   (file.asm - line 13)  401014:	54 
*	As we know that the opcode with start at least only after the third word,
	we loop in that line till the end or till some conditions are met.
	<<These all are just Tweaks to run the code faster and work more efficiently>>
*	We check if the element is has length 2 and has valid heexadecimal syntax.
	Ex:  (line) 401026:	02 66 d1             	add    -0x2f(%esi),%ah
	For "66" or "d1", as they are valid hex syntax, we just skip comparision with them
	(Also, another necessary condition is that our opcodeList doesnt contain any
	two - letter opcode which has a valid hexadecimal syntax)
*	We check if the that word starts with "$","0x", "*","-" or "(":
	indicating a register, variable, negation or anything that cannot be an opcode.
	EX: (line)  401026:	02 66 d1             	add    -0x2f(%esi),%ah  >>>>>> "-" in this line
	  			401065:	3d 02 66 8b d0       	cmp    $0xd08b6602,%eax >>>>>> "$" in this case
				401071:	41                   	inc    %exc         	>>>>>> "%" in this case
				401072:	02 66 25             	add    0x25(%esi),%ah 	>>>>>> "0x" in this case
				401242:	ff 25 b0 10 40 00    	jmp    *0x4010b0        >>>>>> "*" in this case
				401628:	6d                   	insl   (%dx),%es:(%edi) >>>>>> "(" in this case

*	We maintain a count till three as I have seen *maximum* of 3 opcodes occuring in a single line.
	There are very very few instances of 4 opcodes, which we can safetly ignore.
	Ex: (line)   403b75:	f3 89 f4             	repz mov %esi,%esp >>>>>> 2 opcodes
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
		if line:
			splitter = line.split()
			if len(splitter)>2:
				count=0

				for j in xrange(2,len(splitter)):
					a=splitter[j]
					if len(a)==2:
						if CheckHex(a):
							continue

					if a[:1]=='$' or a[:2]=='0x' or a[:1]=='%' or a[:1]=='*' or a[:1]=='-' or a[:1]=='(':
						break

					if count <3:
						if a in opcodes:
							number[opcodes.index(a)]+=1
					else: break
					count+=1


	outfile.write( ",".join(str(x) for x in number))
	outfile.write("\n")
	f1.close()

outfile.close()
