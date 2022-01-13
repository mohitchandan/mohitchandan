xin = 0
y = 0
cnt = -1
fname = input('Enter file name:')
try:
    xfile = open(fname)
except :
    print('bad file name')
    quit()
for x in xfile :
    if int(x.strip()) > int(y) :
        y = x
        #print (str(x) + 'Increased')
        f = open("c:\\test\\demofile2.txt", "a")
        f.write('Increased' + str(x))
        f.close()
        cnt = cnt + 1
    else :
        y = x
        f = open("c:\\test\\demofile2.txt", "a")
        f.write('Decreased' + str(x))
        f.close()
print (cnt)