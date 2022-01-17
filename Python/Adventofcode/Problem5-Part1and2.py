
fname = ''
if fname == '' :
    fname = 'c:\\test\\InputDay5.txt'
try :
    with open(fname) as xfile :
        fdata = xfile.read().splitlines()
except :
    print ('Invalid file')

print('end')
    

def countpoints(countdiagonallines) :
    allpoints = []
    
    for lines in fdata :
        left, right = lines.split('->')
        x1 , y1 = tuple (map(int, left.split(',')))
        x2 , y2 = tuple (map(int, right.split(',')))
    
        if x1 == x2 or y1 == y2 :
            for vx in range(min(x1,x2), max(x1, x2)+1) :
                for vy  in range(min(y1,y2), max(y1,y2) +1) :
                    allpoints.append((vx,vy))
        else : # for diagonal lines
            if countdiagonallines == 1 :
                incx = 1
                incy = 1
                if x1 > x2 : 
                    incx = -1
                if y1 > y2 : 
                    incy = -1
                vy = y1
                for vx in range(x1, x2 + incx , incx ) :    
                    allpoints.append((vx,vy))
                    vy = vy + incy
    
    countpnt2plus(allpoints)

def countpnt2plus(allpoints):
    counttxt = dict()
    for p in allpoints :
        counttxt[p] = counttxt.get(p,0) + 1
    cntmorethan1 = 0
    for k,v in counttxt.items() :
        if v > 1 :
            cntmorethan1 = cntmorethan1 + 1      
    print(cntmorethan1)

countpoints(1)