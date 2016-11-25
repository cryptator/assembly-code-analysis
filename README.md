#assembly-code-analysis
Python scripts for analyzing intel assembly language codes(.asm) using opcode frequency and other means.

#Opcode Frequency scanner for Assembly codes generated from IDA Pro and Objdump

```
usage:
python ASM_to_Frequency_IDA.py -d DIRECTORY -o OUTFILE
python ASM_to_Frequency_objdump.py -d DIRECTORY -o OUTFILE

Output a csv file containing the frequency of all opcodes for each .asm file
in the specified directory.

Required arguments:
  -d folder, --DIRECTORY folder		Location of directory(folder) to scan for .asm files
                        
  -o OUTFILE, --outfile OUTFILE		Name of the output .csv file

Example: python ASM_to_Frequency_IDA.py -d /home/user/malwares/IDA -o malware_freq.csv

```

**opcodeList.txt** contains all the opcodes that we are required to scan


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
