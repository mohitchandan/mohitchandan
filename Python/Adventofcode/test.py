fname = ''#input ('Enter File Name')
_mlist = list()
_xlst  = list()

def writetofile(mlist,name) :
    fname = 'c:\\test\\'+name +'.txt'
    try :
        xfile1 = open(fname ,'a')
    except :
        print ('Invalid file' )
      
    for i in mlist :
        xfile1.write(i + '\n')
    xfile1.close()
    
   
def readfiledataintolist(a1) :
    mlist = list()
    pt = a1.find('-')
    xy = a1[:pt].strip().split(',')
    xy1 = a1[pt + 2 :].strip().split(',')
    x1 = xy
    x2 = xy1
    a = int(x1[0])
    b = int(x2[0])
    c = int(x1[1])
    d = int(x2[1])
    if (a == b and c != d) or (c == d and a != b) :
        
        if a < b :
            for i in range (a , b + 1 ):
                if  not (str(i) +',' + x1[1]) in mlist :
                    mlist.append( str(i) +',' + x1[1])
        else :
            if a!= b :
                for i in range (a , b - 1 , -1):
                    if  not (str(i) +',' + x1[1]) in mlist :
                        mlist.append(  str(i) +',' + x1[1]) 
        if c < d :
            for i in range (c , d + 1):
                if  not (x1[0] +',' + str(i)) in mlist :
                        mlist.append( x1[0] +',' + str(i))
        else :
            if c != d :
                for i in range(c , d - 1, -1):
                    if  not (x1[0] +',' + str(i)) in mlist :
                        mlist.append( x1[0] +',' + str(i))
        
    # diagonal line
    elif 1 == 0:
          
        if a < b and c < d and a == c:
            i = a
            while i < b :
                for i1 in range (c , d + 1 ):
                    if  not (str(i) +',' + str(i1)) in mlist :
                        mlist.append( str(i) +',' + str(i1))
                        if i < b :
                            i = i + 1
        elif a > b and c > d and b == d : 
            i = a
            while b < i :
                for i1 in range (c , d - 1, -1 ):
                    if  not (str(i1) +',' + str(i)) in mlist :
                        mlist.append( str(i1) +',' + str(i))
                        if b < i :
                            i = i - 1
        else :
            i = a
            while b < i :
                if c < d :
                    for i1 in range (c  , d + 1 ):
                        if  not (str(i) +',' + str(i1)) in mlist :
                            mlist.append( str(i) +',' + str(i1))
                            if b < i :
                                i = i - 1 
                else :
                    for i1 in range (c , d - 1, -1  ):
                         if  not (str(i1) +',' + str(i)) in mlist :
                            mlist.append( str(i) +',' + str(i1))
                            if b < i :
                                i = i - 1    
            if  i < b :
                while i < b :
                    if c < d :
                        for i1 in range (c  , d + 1 ):
                            if  not (str(i) +',' + str(i1)) in mlist :
                                mlist.append( str(i) +',' + str(i1))
                                if i < b :
                                    i = i + 1
                    else :
                        for i1 in range (c , d - 1, -1  ):
                             if  not (str(i1) +',' + str(i)) in mlist :
                                mlist.append( str(i) +',' + str(i1))
                                if i < b :
                                    i = i + 1      
    for k in  mlist :
        _mlist.append(k)
    #print (a1)
    
    _xlst.append(a1.rstrip('\n') + ':' + str(len(mlist)))
    if len(mlist) < 1 :
        print(a1,len(mlist))
    writetofile(mlist,'Day5out')



def readvalcnts() :      

    counttxt = dict()
    # fname = 'c:\\test\\Day5out.txt'
    # try:
    #     fhand = open(fname)
    # except:
    #     print('File cannot be opened:', fname)
    #     exit()
    cnt = 0
    # for line in fhand:
    #     _mlist.append(line)
    # #print(len(_mlist))
    for w in _mlist :
        cnt = cnt + 1
        counttxt[w] = counttxt.get(w.strip(),0) + 1
        #print(cnt)
    print(len(counttxt))
    cntmorethan1 = 0
    
    for k in counttxt :
        if counttxt[k] > 1 :
            cntmorethan1 = cntmorethan1 + 1      
    return (cntmorethan1)

def cntfileline () :
    fname = 'c:\\test\\Day5out.txt'
    try:
        fhand = open(fname)
    except:
        print('File cannot be opened:', fname)
        exit()
    cnt1 = 0
    counts = dict()
    for line in fhand:
        words = line.rstrip('\n')
        if words not in counts:
            counts[words] = 1
        else:
            counts[words] += 1
            cnt1 = cnt1 + 1
    # print(len(counts))
    print(cnt1)
    filehandler = open('c:\\test\\Day5out-cnt.txt', 'wt')
    # data = str(counts)
    # filehandler.write(data)
    
    for key, value in counts.items(): 
        filehandler.write('%s:%s\n' % (key, value))

    filehandler.close()
    #print(counts)


def readfile(fname) :
    if fname == '' :
        fname = 'c:\\test\\InputDay5.txt'
    try :
        xfile = open(fname)
    except :
        print ('Invalid file')

    for x in xfile :
        readfiledataintolist(x)
    print('end')

readfile(fname)


#print(_mlist)

cntfileline ()
finalcount = readvalcnts()
print('Two lines overlap at points: ' + str(finalcount))
for x in _xlst :
    print(x)


