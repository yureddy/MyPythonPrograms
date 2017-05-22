line = open("radishsurvey.txt")
line = line.readline()
line = line.strip()
parts = line.split(" - ")
name, vote = parts

print(parts)
print(name)
print(vote)


a,b,c = [1,'king','for all']
print(c)
print(b)
print(a)


name,verb,adjective,e,f,g = "King Solmon, had eaten, BIgger Things".split(' ')
print(adjective)
print(verb)
print(name)
print(e)
print(f)
print(g)

Lauda,lodi,j,k= "King Solmon, had eaten, BIgger Things".split(' ',3)
print(Lauda)
print(lodi)
print(j)
print(k)

print('to count the number of votes for White Icicle radishes')


def CountVotesFor(typevalue):
	print("the number of votes for"+ typevalue + " is ..")
	TotalVotesforWhiteIcicle =0
	for EachLine in open("radishsurvey.txt"):
		EachLine= EachLine.strip()
		BrokenLine = EachLine.split(' - ')
		NameGiven, votedFor = BrokenLine
		if votedFor == typevalue:
			TotalVotesforWhiteIcicle= TotalVotesforWhiteIcicle+1

	return TotalVotesforWhiteIcicle


print(CountVotesFor("Daikon"))
print(CountVotesFor("Sicily Giant"))
print(CountVotesFor("White Icicle"))



print("I am making a dictinary of all votes")

def totalCounter(filename):
	DictionaryofVotes ={}
	for eachline in open(filename):
		eachline = eachline.strip()
		BrokenParts = eachline.split(' - ')
		Name, Votes = BrokenParts
		if Votes not in DictionaryofVotes:
			DictionaryofVotes[Votes]= 1
		else:
			DictionaryofVotes[Votes] = DictionaryofVotes[Votes]+1
	return DictionaryofVotes

ToBePrinted = totalCounter('radishsurvey.txt')

for name in ToBePrinted:
	countTIk = ToBePrinted[name]
	print(name + ":"+ str(countTIk))



print('Printing the pretty printing pretty printing librarry')

from pprint import pprint
pprint(ToBePrinted)