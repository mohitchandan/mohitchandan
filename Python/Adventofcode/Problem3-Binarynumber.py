# from collections import Counter
 
# def most_frequent(List):
#     occurence_count = Counter(List)
#     return occurence_count.most_common(1)[0][0]
   
# List = [2, 1, 2, 2, 1, 3]
# print(most_frequent(List))
# in excel to validate data =SUMPRODUCT(--MID(A2,LEN(A2)+1-ROW(INDIRECT("1:"&LEN(A2))),1),(2^(ROW(INDIRECT("1:"&LEN(A2)))-1)))
tval = tuple()
lstv = list()
lstv1 = list()
sum = 0
i = 0
xv = ''
xv1 = ''
cnt = 0
cnt1 = 0
fname = input ('Enter File Name')
mcmn = 0
mucmn = ''
if fname == '' :
    fname = 'c:\\test\\InputDay3.txt'
while i <= 4 :
    try :
        xfile = open(fname)
    except :
        print ('Invalid file')
        quit()

    cnt = 0
    cnt1 = 0
    for x in xfile :
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

for lv in range(len(lstv)):
    xv = xv + lstv[lv]

print (xv)
#print (int(xv,2))
for lv1 in range(len(lstv1)):
    xv1 = xv1 + lstv1[lv1]
print (xv1)
print(int(xv,2)*int(xv1,2))
#print (int(xv1,2))
