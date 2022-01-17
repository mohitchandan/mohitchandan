# a = list()
# a = [[22,-1,17,11,-1],
#     [8,-1,23,4,-1],
#     [21,4,14,16,-1],
#     [6,-1,3,18,-1],
#     [1,-1,20,15,-1]]

# x = 4
# del a[0]

# c = 0
# col = 0
# bcnt = 0

# def bingo() :
#     print ('biongo')
#     quit()
# for i in range(len(a)) :
#     while c <= x :
#         if  col == 5 :
#             break
#         print (a[c][col])
#         if a[c][col] == -1 :
#             bcnt = bcnt + 1
#             if bcnt == 5 :
#                 bingo()                
#         c = c + 1
#         if c == 5 :
#             c = 0
#             bcnt = 0
#             col = col + 1
a1 ='31,97 -> 857,923'
pt = a1.find('-')
xy = a1[:pt].strip().split(',')
xy1 = a1[pt + 2 :].strip().split(',')
x1 = xy
x2 = xy1
_mlist = list()
a = int(x1[0])
b = int(x2[0])
c = int(x1[1])
d = int(x2[1])
if (a == b) or (c == d) :
    if a < b :
        for i in range (a , b + 1 ):
            if  not (str(i) +',' + x1[1]) in _mlist :
                _mlist.append( str(i) +',' + x1[1])
    else :
        if a!= b :
            for i in range (a , b - 1 , -1):
                if  not (str(i) +',' + x1[1]) in _mlist :
                    _mlist.append(  str(i) +',' + x1[1]) 
    if c < d :
        for i in range (c , d + 1):
            if  not (x1[0] +',' + str(i)) in _mlist :
                    _mlist.append( x1[0] +',' + str(i))
    else :
        if c != d :
            for i in range(c , d - 1, -1):
                if  not (x1[0] +',' + str(i)) in _mlist :
                    _mlist.append( x1[0] +',' + str(i))
else : # diagonal line
    
    if a < b and c < d and a == c:
        
        i = a
        while i < b :
            for i1 in range (c , d + 1 ):
                if  not (str(i) +',' + str(i1)) in _mlist :
                    _mlist.append( str(i) +',' + str(i1))
                    if i < b :
                        i = i + 1
    elif a > b and c > d and b == d : 
        i = a
        while b < i :
            for i1 in range (c , d - 1, -1 ):
                if  not (str(i1) +',' + str(i)) in _mlist :
                    _mlist.append( str(i1) +',' + str(i))
                    if b < i :
                        i = i - 1
    else :
        i = a
        while b < i :
            if c < d :
                for i1 in range (c  , d + 1 ):
                    if  not (str(i) +',' + str(i1)) in _mlist :
                        _mlist.append( str(i) +',' + str(i1))
                        if b < i :
                            i = i - 1 
            else :
                for i1 in range (c , d - 1, -1  ):
                     if  not (str(i1) +',' + str(i)) in _mlist :
                        _mlist.append( str(i) +',' + str(i1))
                        if b < i :
                            i = i - 1            
        while i < b :
            if c < d :
                for i1 in range (c  , d + 1 ):
                    if  not (str(i) +',' + str(i1)) in _mlist :
                        _mlist.append( str(i) +',' + str(i1))
                        if i < b :
                            i = i + 1 
            
            else :
                for i1 in range (c , d - 1, -1  ):
                     if  not (str(i1) +',' + str(i)) in _mlist :
                        _mlist.append( str(i) +',' + str(i1))
                        if i < b :
                            i = i + 1 
       
                    
    

#_lst.append(str(xy1))
print(_mlist)
#print(_minx, _miny)

# counttxt = dict()
# for w in _lst :
#     counttxt[w] = counttxt.get(w,0) + 1
# print (counttxt)