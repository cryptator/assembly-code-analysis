#assembly-code-analysis
Python scripts for analyzing intel assembly language codes(.asm) using opcode frequency.   
<br />
Running the script on a folder containing .ASM files will output a CSV file with the first row containing the index of the opcode in the **opcodeList.txt** file and the first column will contain the name of each file, followed by the frequency of each opcode that occurs in the list.
<br />
**opcodeList.txt** contains all the opcodes that we are required to scan
<br />
Example: If we have a folder to scan with 100 .ASM/asm files and our opcode list contains 1808 opcodes, 
the output table format (CSV):

Filename| 1 | 2 | 3 | 4 | 5 | ..... | 1808  
0.ASM | 0 | 0 | 5 | 4 | 0 | ..... | 0  
1.ASM | 0 | 3 | 0 | 2 | 1 | ..... | 13  
... | ... | ... | ... | ... | ... | ... | ...  
99.ASM | 13 | 3 | 5 | 42 | 0 | ..... | 0  
  
#Opcode Frequency scanner for Assembly codes generated from IDA Pro and Objdump

```
usage:
python ASM_to_Frequency.py -d DIRECTORY -o OUTFILE
python ASM_to_Frequency_objdump.py -d DIRECTORY -o OUTFILE

Output a csv file containing the frequency of all opcodes for each .asm file
in the specified directory.

Required arguments:
  -d folder, --DIRECTORY folder		Location of directory(folder) to scan for .asm files
                        
  -o OUTFILE, --outfile OUTFILE		Name of the output .csv file

Example: python ASM_to_Frequency.py -d /home/user/malwares/IDA -o malware_freq.csv

```


<br />
#Windows executables(.exe) to Assembly Language(.asm) Script using objdump


```
usage:
python exe_to_assembly_objdump.py -d DIRECTORY

Use objdump to scan specfied folder for .exe files and dissamble them, i.e. convert to .asm files.

Required arguments:
  -d DIRECTORY, --directory DIRECTORY	Location of folder to scan for .exe files

Example: python exe_to_assembly_objdump.py -d /home/user/malwares/exe
```

The script will save the assembly codes of all ".exe" files scanned in the specified directory to a new directory named "assembly_codes" and will move the files which it cannot disassemble to a directory named "objdump_error"
