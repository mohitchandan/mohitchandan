xin = 0
y = 0
cnt = 0
sm = 0  
a = 0
b = 3
lsti = list()
listsum = list()
fname = input('Enter file name:')
try:
    xfile = open(fname)
except :
    print('bad file name')
    quit()
for x in xfile :
    lsti.append(int(x.strip()))
#print (lsti)
for i in range(len(lsti)) :  
    if i == 0 :
        listsum.append(sum(lsti[a:b]))
    a = a + 1
    b = b + 1
    listsum.append(sum(lsti[a:b]))
    # if a == 10 : # to check less values
    #     break
#print (listsum)
for sm in range(len(listsum)) :
    if int(listsum[sm]) > int(y) :
        y = listsum[sm]        
        f = open("c:\\test\\demofile2.txt", "a")   
        if sm == 0 :
            f.write('Start ' + str(listsum[sm]) + '\n')  
        else :
            f.write('Increased ' + str(listsum[sm]) + '\n')
            cnt = cnt + 1
        f.close()
        #print ('Increased ' + str(listsum[sm]) )        
    else :
        y = listsum[sm]
        f = open("c:\\test\\demofile2.txt", "a")
        f.write('Decreased ' + str(listsum[sm]) + '\n')
        f.close()
        #print ('Decreased ' + str(listsum[sm]) )
print (cnt)


