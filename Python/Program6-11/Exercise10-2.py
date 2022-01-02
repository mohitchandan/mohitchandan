# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

wrdlist = list()
hourlst = list()
cntdict =  dict()
hour = ''
fname = input('Enter filename')
mrep = None
mcnt = 0
try :
    xfile = open(fname)
except :
    print('Enter valid filename')
    quit()

for x in xfile :
    if x.startswith('From ') :
        wrdlist = x.split()
        hour = wrdlist[5].split(':')[0]
        #print (hour)
        cntdict[hour] = cntdict.get(hour , 0) + 1
#print(sorted(cntdict.items()))
for (k,v) in sorted(cntdict.items()) :
    print (k,v)
# for (k,v) in cntdict :
#     newtp = (k,v)

#     hourlst.append()
# print(hourlst)






