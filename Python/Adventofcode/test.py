fname = ''#input ('Enter File Name')
_mlist = list()
_dctval = dict()


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
    for i in mlist :
        _mlist.append(i)


def readvalcnts() :  
    counttxt = dict()
    for w in _mlist :
        counttxt[w] = counttxt.get(w,0) + 1
    
    for k in counttxt :
        print (k , counttxt[k])

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
print(_mlist)
readvalcnts()