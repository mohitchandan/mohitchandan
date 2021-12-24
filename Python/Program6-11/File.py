fname = input('Enter file name:')
try:
    xfile = open(fname)
except :
    print('bad file name')
    quit()

for x in xfile :
    if not x.startswith('to') :
        continue
    else:
        print(x.rstrip())

#witnin line
count = 0

xfile = open('C:\\test\\input.txt')
for x in xfile :
    count = count +1 
    if  '@' not in x :
        continue
    else:
        print(x.rstrip())
print(count)
