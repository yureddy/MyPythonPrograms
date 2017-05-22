with open('sampleUTF16.txt','r',encoding ='utf-8') as infile:
	next = infile.read(100)
with open('UTF16_delete2.txt','w',encoding ='utf-8') as infile2:
	infile2.write(next)
