fdist = 0
cnt = 0
cnt1 = 0
lfwd = 0
depth = 0
depth1 = 0
txtline = ''
aim = 0
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
    lfwd = 1
    #print(txtline[0],txtline[1])
    if txtline[0] == 'forward':
        depth1 = 0
        fdist = fdist + int(txtline[1])
        #print ('depth ' + str(depth))
        depth1 =  (int(txtline[1]) * aim)
        depth = depth  + depth1
        #print (txtline[0] + txtline[1] +' aim ' + str(aim) + ' depth1 ' + str(depth1) + ' depth ' +  str(depth))    
    elif txtline[0] == 'down':
        cnt1  = cnt1 + 1
        #print(txtline[0] +txtline[1]+'depth ' +str(depth))
        #depth = depth + int(txtline[1]) + depth1
        aim =  aim + int(txtline[1])
        #print(txtline[0] +txtline[1]+' aim' + str(aim) + ',cnt ' + str(cnt1),'depth ' +str(depth) +' depth1 ' +str(depth1))
    elif  txtline[0] == 'up':
        #depth = depth - int(txtline[1])
        aim = aim - int(txtline[1])
        #print(txtline[0] +txtline[1]+' aim' + str(aim) + ',cnt ' + str(cnt1))
    # if cnt == 6 : #testset
    #     break
#depth = depth + depth1
#print ('final depth ' +str (depth))
print(depth * fdist)
# print (fdist,depth,lfwd)
#print (fdist , depth)
