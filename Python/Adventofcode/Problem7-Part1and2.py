#Imports
from statistics  import median

fname = ''
if fname == '' :
    fname = 'c:\\test\\InputDay7.txt'
try :
    with open(fname) as xfile :
        fdata = xfile.read().splitlines()
except :
    print ('Invalid file')

print('end')

#part1
def submoves() :
    fluelspent = 0 
    input = list(map(int,fdata[0].split(',')))
    input.sort()
    mfluelspent = 0
    #print (range(min(input),max(input)))
    for r in range(min(input),max(input)) :
        #print('pos to move :'+ str(r))
        fluelspent = 0 
        for p in input :
            val = abs( int(p) -  r) 
            fluelspent += val
            #print (val)
        #print ('fluelspent :' + str(fluelspent))
        if fluelspent < mfluelspent or mfluelspent == 0:
            mfluelspent = fluelspent
    print ('cheapest possible outcome :' + str(mfluelspent))

#part2
def submoveschanges() :
    fluelspent = 0 
    input = list(map(int,fdata[0].split(',')))
    input.sort()
    mfluelspent = 1 << 100
    #print (range(min(input),max(input)))
    for r in range(min(input),max(input)) :
        #print('pos to move :'+ str(r))
        fluelspent = 0 
        for p in input :
            positiontoreach = abs(int(p) - r) + 1
            #print(p,r )
            #print (range(1, positiontoreach ))
            val = sum(range(1, positiontoreach ))
            fluelspent += val
            #print (val)
        #print ('fluelspent :' + str(fluelspent))
        mfluelspent = min(mfluelspent, fluelspent)
        # if fluelspent < mfluelspent or mfluelspent == 0:
        #     mfluelspent = fluelspent
    print ('cheapest possible outcome :' + str(mfluelspent))

def part1bymedian() :
    fuelspent  = 0
    input = list(map(int,fdata[0].split(',')))
    med = int(median(input))
    for i in input :
        fuelspent +=  abs(i - med)
    print('cheapest possible outcome :' + str(fuelspent))
part1bymedian()    
#part2
submoveschanges()
##Part1
#submoves()

