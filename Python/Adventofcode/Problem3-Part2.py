# from collections import Counter
 
# def most_frequent(List):
#     occurence_count = Counter(List)
#     return occurence_count.most_common(1)[0][0]
   
# List = [2, 1, 2, 2, 1, 3]
# print(most_frequent(List))
# in excel to validate data =SUMPRODUCT(--MID(A2,LEN(A2)+1-ROW(INDIRECT("1:"&LEN(A2))),1),(2^(ROW(INDIRECT("1:"&LEN(A2)))-1)))


slen = 11

def readfile(fname) :
    lstx = list()
    
    try :
         xfile = open(fname)
    except :
        print ('Invalid file')
        quit()
    for x in xfile :
        lstx.append(x.strip())
    return (lstx)

def getcommoninlist(lst1in, gvmecommon) :
    i = 0
    lstv1 = list()
    lstv = list()
    xv = ''
    xv1 = ''
    while i <= slen :
        cnt = 0
        cnt1 = 0
        for x in lst1in :
            tval = tuple(x)
            if tval[i] == '1' : 
                cnt1 = cnt1 + 1
            if tval[i] == '0' : 
                cnt = cnt + 1   
        if cnt1 < cnt :
            lstv.append('0')
            lstv1.append('1')             
        else :
            lstv.append('1')
            lstv1.append('0')   
        i = i + 1
    #mostcommon
    for lv in range(len(lstv)):
        xv = xv + lstv[lv]
    #print (xv)
    #most uncommon
    for lv1 in range(len(lstv1)):
        xv1 = xv1 + lstv1[lv1]
    #print (xv1)
    if gvmecommon == 1: 
        return(lstv)
    else :
        return(lstv1)
   
def refnelistbycommon( lstin2 ,ncommon) :
    i = 0
    lstco2 = list()
    lstco2 = lstin2
    
    #print (lstv)
    #print(lstco2)
    xtup = tuple(lstco2)
    while i <= slen :
        lstvo = getcommoninlist(lstco2 , ncommon)
        #for a1 in range(len(xtup)):
        for word in lstco2[:]:
            #print (lstv[i])
            if not word[i:].startswith(lstvo[i]):
                #print(lstco2)
                lstco2.remove(word)
                #print(lstco2)

                if len(lstco2) == 1 :
                    return(lstco2)
                    quit()
       
        i= i + 1

    return(lstco2)


#lstvo = getcommoninlist(lst1)
fname = input ('Enter File Name')
if fname == '' :
    fname = 'c:\\test\\InputDay3.txt'
lst1 = readfile(fname)
ox = refnelistbycommon(lst1, 1)
oxygengeneratorrating = ox
print (oxygengeneratorrating,int(oxygengeneratorrating[0],2))

lst2 = readfile(fname)
cos2scrubberrating = refnelistbycommon(lst2, 0)
print(cos2scrubberrating, int(cos2scrubberrating[0],2))

print('life support rating: ' + str(int(oxygengeneratorrating[0],2) * int(cos2scrubberrating[0],2)))
