# Write a program which repeatedly reads numbsderffs until the
# user enters “done”. Once “done” is entered, print out the total, count,
# and average of the numbers. If the user enters anything other than a
# number, detect their mistake using try and except and print an error
# message and skip to the next number.

def uinput() :
    cnt = 0
    tot = 0.0
    while True :
        inputvalue = input("Enter Number:")
        if (inputvalue == "done") :
            break
        try :
            iinputvalue = int(inputvalue)
        except :
            print("Enter a valid number")
            continue
        cnt = cnt + 1
        tot = tot + iinputvalue
    return("total: " + str( tot), "Count: "  + str(cnt), " Average: " + str(tot/cnt))

finaloutput=uinput()
print (finaloutput)

