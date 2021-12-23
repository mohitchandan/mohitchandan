# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
# Once 'done' is entered, print out the largest and smallest of the numbers. 
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
# Enter 7, 2, bob, 10, and 4 and match the output below.

def uinput() :
    cnt = 0
    fo = 0
    iinputvalue = None
    lar =  None
    smal = None
    while True :
        inputvalue = input("Enter Number:")
        if (inputvalue == "done") :
            break
        else :
            try :
                iinputvalue = int(inputvalue)
                if (lar is None) :
                    lar = iinputvalue
                elif (iinputvalue > lar) :
                    lar = iinputvalue
                #small    
                if (smal is None) :
                    smal = iinputvalue
                elif (iinputvalue < smal) :
                    smal = iinputvalue
            except :
                print("Invalid input")
                continue
            
    return(lar,smal)        
        

finaloutput=uinput()
print ("Maximum is " + str(finaloutput[0]))
print ("Minimum is " +str(finaloutput[1]))

print("Hello World")