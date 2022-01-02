# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

wrdlist = list()
cntdict =  dict()
email = ''
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
        email = wrdlist[1]
        cntdict[email] = cntdict.get(email , 0) + 1
for k,v in cntdict.items() :
    if mrep is None or v > mcnt :
        mrep = k
        mcnt = v
#print(cntdict)
print (mrep, mcnt)