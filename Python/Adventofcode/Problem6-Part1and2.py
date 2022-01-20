input =  [3,5,1,5,3,2,1,3,4,2,5,1,3,3,2,5,1,3,1,5,5,1,1,1,2,4,1,4,5,2,1,2,4,3,1,2,3,4,3,4,4,5,1,1,1,1,5,5,3,4,4,4,5,3,4,1,4,3,3,2,1,1,3,3,3,2,1,3,5,2,3,4,2,5,4,5,4,4,2,2,3,3,3,3,5,4,2,3,1,2,1,1,2,2,5,1,1,4,1,5,3,2,1,4,1,5,1,4,5,2,1,1,1,4,5,4,2,4,5,4,2,4,4,1,1,2,2,1,1,2,3,3,2,5,2,1,1,2,1,1,1,3,2,3,1,5,4,5,3,3,2,1,1,1,3,5,1,1,4,4,5,4,3,3,3,3,2,4,5,2,1,1,1,4,2,4,2,2,5,5,5,4,1,1,5,1,5,2,1,3,3,2,5,2,1,2,4,3,3,1,5,4,1,1,1,4,2,5,5,4,4,3,4,3,1,5,5,2,5,4,2,3,4,1,1,4,4,3,4,1,3,4,1,1,4,3,2,2,5,3,1,4,4,4,1,3,4,3,1,5,3,3,5,5,4,4,1,2,4,2,2,3,1,1,4,5,3,1,1,1,1,3,5,4,1,1,2,1,1,2,1,2,3,1,1,3,2,2,5,5,1,5,5,1,4,4,3,5,4,4]
#input = [3,4,3,1,2]
print (len(input))
_days = 256000

#part1 no perf method will not work for 256 rows
def fishtime() :
    day = _days
    fishes = input
    while day > 0 :
        for i in range(len(fishes)) :
            if fishes[i] == 0 : 
                fishes[i] = 6
                fishes.append(8)
            else :
                fishes[i] -= 1
        day -= 1
        print(day)
        #print (fishes)
        
        if day == 0 :
            print('On day ' + str(day) + ', total fises are :' + str(len(fishes)))  

# perf tuned method
def part2() :
    ix = 0
    dctfishes = dict({8:0,7:0, 6:0 ,5:0, 4:0, 3:0 ,2:0, 1:0, 0:0})
    for p in input :
        dctfishes[p] = dctfishes.get(p,0) + 1
    day = _days
    while day > ix :
        x = dctfishes[0]
        dctfishes[0] = dctfishes[1]  
        dctfishes[1] = dctfishes[2]  
        dctfishes[2] = dctfishes[3]  
        dctfishes[3] = dctfishes[4]   
        dctfishes[4] = dctfishes[5]  
        dctfishes[5] = dctfishes[6]  
        y = dctfishes[7]
        if dctfishes[0] == 0  or x > 0:
            dctfishes[6] = dctfishes[7] + x   
        else :
            dctfishes[6] = y
        dctfishes[7] = dctfishes[8]  
        dctfishes[8] = x   
        ix += 1
    print(sum(dctfishes.values()))


#part1 only for small input
#fishtime()
#for large values
part2()
#testinputcnt()