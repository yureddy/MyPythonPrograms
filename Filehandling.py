fp = open("MyFirstFile.txt","r+")
#print(fp)

#fp.write("**** I am writing from the program Filehandling.py**** \n")
#fp.write("****This is second line i am writeing from a program to MyFirstFile.txt*****")


#print("I am printing fp.read")
#print(fp.read())

print("I am printing fp.readline")
print(fp.readline())

print("I am printing fp.readlines")
print(fp.readlines())


Lines_oF_Text = ['**New Line 1 Added** \n', '**New Line 2 Added** \n','**New Line 3 Added** \n']
fp.writelines(Lines_oF_Text)
fp.close()


