# dictionaries
# way 1
def dict1() :
    counts = dict()
    names = ['raj','ram','ajay','raj','Ram','sum','ajay','ram','ajay','raj']
    for name in names :
        if name not in counts :
            counts[name] = 1
        else :
            counts[name] = counts[name] +1
    counts['kris'] =  1
    print(counts)
    print ('count of Kris is ' ,counts['kris'])
    
    # way 2 without if
    counts1 = dict()
    names1 = ['raj','ram','ajay','raj','Ram','sum','ajay','ram','ajay','raj']
    for name1 in names1 :
        counts1[name1] = counts1.get(name1,0) + 1    
    print(counts1)

# count in file or input txt
counttxt = dict()
def dict2() :
    print ('enter text')
    txtin = input('')
    wordsintxt = txtin.split()
    wordsintxt.sort()
    print (wordsintxt)
    for w in wordsintxt :
        counttxt[w] = counttxt.get(w,0) +1

    print (counttxt)
    for k in counttxt :
        print (k , counttxt[k])
    # convert to list
    print (list(counttxt))
    # convert to list for keys
    print (list(counttxt.keys()))
    # print list values
    print (list(counttxt.values()))
    
    print (counttxt.items())
    for k,v in counttxt.items() :
        print(k,v)

#dict2()
wrdlist = list()
cntdict = dict()
wrdlist1 = list()

def countwordsinfile() :
    bigword = None
    bigcount = 0
    cnt = 0
    fname = input('enter file name:')
    try :
        xfile = open(fname)
    except :
        print('bad file name')
        quit()
    for x in xfile:
        wrdlist = x.split()
        # for w in range(len(wrdlist1)) :
        #     wrdlist.append(wrdlist1[w])
        for wrds in wrdlist :
            cntdict[wrds] = cntdict.get(wrds , 0) + 1
    print (cntdict)

# find most reprated word
    for k,v in cntdict.items() :
        if bigword is None or v > bigcount :
            bigcount = v
            bigword = k
    print ('Most repeated word is: ' + bigword + ', and have a count: ', bigcount)
    
countwordsinfile()