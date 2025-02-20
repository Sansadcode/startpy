#program to give assertion message when input is not what the program asked for

def checkvalue(valuetocheck):
    assert (type(valuetocheck) is int), "you must enter a number:"
    assert (valuetocheck > 0), "value entered must be greater thatn 0"
    if valuetocheck > 4:
        print("value is greater than 4")
var = int(input("enter a number greater than 0:"))
checkvalue(var)