MyString = "na peru Yugandhar\treddy red raj"

print(MyString.format())

print("Usage of str.capitalize() on   " + MyString)
print(MyString.capitalize())

print("using of casefolding")
print(MyString.casefold())

print('usage of str.centre(width)')
print(MyString.center(100))

print('usage of str.centre(width,[,filchar])')
print(MyString.center(100,'*'))

print('usage of str.count(sub[,start[,end]]')
print(MyString.count('ed',0,27))

print('usage of str.encode(encoding = "utf-8",errors="strict"')
print(MyString.encode(encoding="utf-8",errors="strict"))

print('usage of str.encode(encoding = "utf-16",errors="strict"')
print(MyString.encode(encoding="utf-16",errors="strict"))

print('usage of str.encode(encoding = "ASCII",errors="strict"')
print(MyString.encode(encoding="ASCII",errors="strict"))

print("str.endswith(suffix[,start[,end]])")
print(MyString.endswith("ar",1,17))

print("str.expandstabs(tabsize =8) # I think it just expanding the tab, varibale length") 
print(MyString.expandtabs(tabsize=8))

print('usage of str,find(sub[,start[,end]]')
print(MyString.find('er',1,31))

print("str.format is like scanf in C programming")
MyString2 = "{Variable1} is the king of {variable2} Kingdom"
print(MyString2.format(Variable1='Yugandhar', variable2='Mahishmathi'))
print(MyString2.format(Variable1=1,variable2=2))
print(MyString2.format(Variable1=[1,2],variable2={'1':'2','king':'of kings'}))
print("Mixing references to positional and keyword arguments")
MyString3 = "the {0} is the {1} solution of {variable4}"
print(MyString3.format(2,'king',variable4='stupidity'))

print('usage of str.index(sub[,start[,end]]')
print(MyString.index('red',0,31))

print('usage of str.isalnum()')
print(MyString.isalnum())
ANString='def \nsadasda\tcdsaads\asada'
print(ANString.isalnum())
print('usage of str.isalpha()')
print(ANString.isalpha())
print('usage of str.isdecimal()')
print(ANString.isdecimal())
print('usage of str.isdigit()')

print('to use str.isidentifier()')
print(ANString.isidentifier())

print('touse keyword.iskeyword()')
#print(ANString.iskeyword())

print('to check str.islower() , to check all the char in str are lowercase')
print(ANString.islower())

print('usage of str.isprintable()- True if all char in string are printable')
print('Non printable char are the on in Unicode characterdatabase as - other-Separator')
print(ANString.isprintable())

print('is usage of str.isspace()')
print(ANString.isspace())