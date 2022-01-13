fdist = 0
cnt = 0
depth = 0
txtline = ''
fname = input ('Enter File Name')
if fname == '' :
    fname = 'c:\\test\\InputDay2.txt'

try :
    xfile = open(fname)
except :
    print ('Invalid file')
    quit()

for x in xfile :
    cnt = cnt + 1
    txtline = x.split()
    #print(txtline[0],txtline[1])
    if txtline[0] == 'forward':
        fdist = fdist + int(txtline[1])
    elif txtline[0] == 'down':
        depth = depth + int(txtline[1])
    elif  txtline[0] == 'up':
         depth = depth - int(txtline[1])
    # if cnt == 6 :
    #     break
#print (fdist,depth)
print (fdist * depth)
