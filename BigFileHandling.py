

input = open('BigtextFile.txt','r')
Output_File = open('output1.txt','w')

#while(1):
for lines in range(100000000000000000000000):
		line = input.readline()
		Output_File.write(line)
	#user_input = input("Type Stop to Quit, else press any key to continue")
	#if user_input == 'STOP':
	#	break



#To run OS commands from Python
#import os
#ToIdentify = os.system('ls -la')
#print(ToIdentify)

#Copying from one file and creating and writing the whole content to it
#pass the command line as  ##$"python Filehandling.py MyFirstFile.txt Duplicate.txt"
#import sys
#f len(sys.argv) < 3:
#	print("wrong Prameter")
#	print("Give the console command in the form python Filehandling.py file1 file2")
#	sys.exit()

#print("you have entered sys.argv[0] is "+sys.argv[0] + "sys.argv[1] is" +sys.argv[1]+ "sys.argv[2] is"+sys.argv[2] )
#f1 = open(sys.argv[1])
#File1Content=f1.readlines()
#print(File1Content)
#f1.close()
#f2 = open(sys.argv[2],'w')
#f2.writelines(File1Content)
#f2.close()



#program which takes 
#files names as inpout from the user and show the 
#content of the files in console

#FilesName = input("Enter the file name ")
#FilesObject = open(FilesName)
#print(FilesObject.read())
#FilesObject.close()



#with open("MyFirstFile.txt") as myNewFilePointer:
#	for line in myNewFilePointer:
#		print (line)
# we dont need to explicitly close a filepointer, if we use with to open file




#if you do not provide any mode, the file will be open in read only mode
#You should always explicitly close the opened file, as there is a limit
#on how many files can be opned at a time on sys, so system can crash if 
#if the limit cross, 
#Each open file consumes some amount of main memoery for data structures
#associated with it like file descriptor/handle or file locks etc,so u
#may end up opening lot of files wasting lot of memory if you have more 
#files that are not useful or usable. Open files stand a chance of 
#curroption and data loss


#*** to show usage of for loop
#fp = open("MyFirstFile.txt","a")
#for line in fp:
  #print(line)

#fp.write("Line 7")
#fp.close()