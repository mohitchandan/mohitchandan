input = [92,12,94,64,14,4,99,71,47,59,37,73,29,7,16,32,40,53,30,76,74,39,70,88,55,45,17,0,24,65,35,20,63,68,89,84,33,66,18,50,38,10,83,75,67,42,3,56,82,34,90,46,87,52,49,2,21,62,93,86,25,78,19,57,77,26,81,15,23,31,54,48,98,11,91,85,60,72,8,69,6,22,97,96,80,95,58,36,44,1,51,43,9,61,41,79,5,27,28,13]
_cardwid = 5
_cards = list()
_card = list()
_input = list()

def create_card(xin,_card) :
    xin1 = xin.split()
    xin1 = [int(i) for i in xin1]
    if  len(xin1) == 0 :
        print(_card)
    _card.append(xin1)


def lucky_card(_card) :
    print(_card)
    #_card.clear()

def cntuncroddnum(cardin2) :
    sum = 0
    for i in range(len(cardin2)) :
        for i1 in range(len(cardin2[i])) :
            if cardin2[i][i1] != -1 :
                sum = sum + int(cardin2[i][i1])
    return(sum)  

fname = ''#input ('Enter File Name')
if fname == '' :
    fname = 'c:\\test\\InputDay4.txt'
try :
    xfile = open(fname)

except :
    print ('Invalid file')
for x in xfile :
    if x.startswith('input:') :
        #print(_input)
        continue
    if not len(x) > 1:
        continue
    create_card(x,_card)
    #print((len(_card)))
    if (len(_card)) == 5 :
        ctrd = _card.copy()    
        _cards.append(ctrd)
        _card.clear()

def checkbingocolumn(cardin) :
    cardin = cardin
    bcnt = 0
    x = 4
    c = 0
    col = 0  
    for i in range(len(cardin)) :
        while c <= x :
            if  col == 5 :
                break
            #print (cardin[c][col])
            if cardin[c][col] == -1 :
                bcnt = bcnt + 1
                if bcnt == 5 :
                    return ('Bingo')                
            c = c + 1
            if c == 5 :
                c = 0
                bcnt = 0
                col = col + 1

    # for i1 in range(len(cardin) ) :    
    #     _cardwid = 0
    #     bcnt = 0
    #     cnt = 0
    #     for lis2 in range(len(cardin[i1])) :
    #         print(cardin[i1])
    #         #for lis21 in range(len(cardin[i1][lis2])) :
    #         print(cardin[i1][lis2])
    #         print(cardin[i1][lis2][_cardwid])  
    #         if cardin[i1][lis2][_cardwid] == -1:
    #             bcnt = bcnt + 1 
    #         cnt = cnt + 1 
    #         if cnt == 5 :
    #             _cardwid = _cardwid + 1
    #             bcnt = 0
    #             cnt = 0
    #         if bcnt == 5 :          

    #             #print('Bingo')
    #             return('Bingo')
    #             #quit()

def checkbingo(_cards) :
    cardin = _cards
    for i1 in range(len(cardin)) :
        for i in range(len(cardin[i1])):
            if sum(cardin[i1][i]) < 1 :
                #print ('Bingo')
                return('Bingo')
                quit()
        bin = checkbingocolumn(cardin[i1])
        if bin == 'Bingo' :
            return('Bingo')

        

        # _cardwid = 0
        # bcnt = 0
        # for lis2 in range(len(cardin[i1])) :
        #     print(cardin[i1])
            
        #     cnt = 0
        #     #for lis21 in range(len(cardin[i1][lis2])) :
        #     print(cardin[i1][lis2])
        #     print(cardin[i1][lis2][_cardwid])  
        #     if cardin[i1][lis2][_cardwid] == -1:
        #         bcnt = bcnt + 1 
        #     cnt = cnt + 1 
        # if bcnt == 5 :
        #     _cardwid = _cardwid + 1
        #     #print('Bingo')
        #     return('Bingo')
        #     #quit()
bingotime = ''

def bingo(card,cardf,i) :
    #print (i)
    #print(cardf)
    wincardsum = cntuncroddnum(cardf)
    print ('Bingo Winner!! Sum of numbers from win card: ' + str(wincardsum) + ' win card: ' + str(card) + ' winNo :' +str(i))
    print(str(wincardsum * i))
    quit()

def bingostart()  :
    for i in input :
        #print(i)
        # if i == 21 :
        #     print('check')
        for a in range(len(_cards)) :
            for b in range(len(_cards[a])) :
                for c in range(len(_cards[a][b])) :
                    if i == int(_cards[a][b][c]) :
                        _cards[a][b][c] = -1
                        bingotime = checkbingo(_cards)
                        if bingotime == 'Bingo' :
                            bingo(a,_cards[a],i)
                        #print('test')
    if bingotime != 'Bingo' :              
        print('No Winner!!!')

#execute to get winner
bingostart()


