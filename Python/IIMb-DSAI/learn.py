def dayofweek(day):
    days = ["Mon","Tue","Wed","Thru","Fri","Sat","Sun"]

    #for day in days:
    if (day == "Fri"):
        print("TGIF")
    elif (day == "Sat" or day == "Sun"):
        print ("Weekend")
    else:
        print("Weekday- yay")

def dayofweek1(day):
    days = ("Mon","Tue","Wed","Thru","Fri","Sat","Sun")

    #for day in days:
    if (day == "Fri"):
        print("TGIF")
    elif (day == "Sat" or day == "Sun"):
        print ("Weekend")
    else:
        print("Weekday- yay")

# dayofweek("Fri")
# dayofweek1("Fri")

def apply_to_list(some_list, func):
    return [func(elt) for elt in some_list]

def sqr_func(x):
    return(x**2)

apply_to_list([1,2,3,4], sqr_func)


[x*2 for x in range(1,3)] # comprehensive list