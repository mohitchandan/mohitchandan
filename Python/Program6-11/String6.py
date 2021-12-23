fruit = "Banana"
for fr in fruit :
    print (fr)


fr1 = 0 
while (fr1 < len(fruit)) :
    print (fruit[fr1])
    fr1 = fr1 + 1

#slicing    
print(fruit[0:3])

if ('n' in fruit ):
    print("yes")

#Case
print(fruit.upper())
print(fruit.lower())

#find position
pos = fruit.find('na')
print(pos)

#replace
nf = fruit.replace('nana','g')
print(nf)

#remove spaces
newtext = "   Hello new fried    "
newtext1 = newtext.rstrip()
newtext2 = newtext.lstrip()
newtext3 = newtext.strip()
print(newtext)
print(newtext1)
print(newtext2)
print(newtext3)

print(fruit.startswith('B'))

#string split
data = "this is my email address email@gmail.com for test"
atpos = data.find('@')
print(atpos)
nspace = data.find(' ',atpos)
print (nspace)
print(data[atpos+1:nspace])


x = 'From marquard@uct.ac.za'
print(x[8])
x = 'From marquard@uct.ac.za'
print(x[14:17])


data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])