

fname = 'c:\\test\\inputday8.txt'
with open(fname) as xfile :
    fdata = xfile.read().splitlines()
valtocheck = [2,3,4,7] # value for easy numbers
digi = dict()
def digi_part1 ():
    valcnt = 0
    for d in fdata :
        pos = d.find('|')
        line = d[pos + 1:].strip().split()
        for l in line :
            digi[len(l)] = digi.get(len(l),0) + 1
            if len(l) in valtocheck :
                valcnt += 1
    print('digits 1, 4, 7, or 8 appear : ' + str(valcnt))



# https://www.programiz.com/python-programming/methods/set/issubset

def digi_part2 ():
    sum = 0

    dctdigists = dict()
    for d in fdata :
        val = ''
        line_left = d[0 : d.find('|') ].strip().split()
        for l in line_left :
            if len(l) == 2 :
                dctdigists[1] = set(l)
                continue
            if len(l) == 3 :
                dctdigists[7] = set(l) 
                continue
            if len(l) == 4 :
                dctdigists[4] = set(l)
                continue
            if len(l) == 7 :
                dctdigists[8] = set(l)  
                continue    
        for l in line_left :
            if len(l) == 6 :
                if dctdigists[4].issubset(set(l)):
                    dctdigists[9] = set(l)
                    continue
                elif dctdigists[1].issubset(set(l)) :
                    dctdigists[0] = set(l)
                    continue
                else :
                    dctdigists[6] = set(l)
                    continue
        for l in line_left :           
            if len(l) == 5 :
                if set(l).issubset(dctdigists[6]):
                    dctdigists[5] = set(l)
                    continue
                elif dctdigists[7].issubset(set(l)):
                    dctdigists[3] = set(l)
                    continue              
                else : 
                    dctdigists[2] = set(l)
                    continue
                
        
        output_val = []
        line_right = d[d.find('|') +1 : ].strip().split()       
        for lr in line_right :
            for key,value in (dctdigists.items()) :
                if set(lr) == set(value) :
                    output_val.append(str(key))
                    break
        output_val = int(''.join(output_val))
        #print(output_val)
    #        for lr in line_right:  
    
        sum += output_val
    return(sum)
#digi_part1 ()
totalval = digi_part2 ()
print('total sum: ' + str(totalval))