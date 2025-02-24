#return without an expression
def happy_new_year(wishes = True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return
    print("Happy New Year!")
happy_new_year(False)

#return with an expression
def boring_function():
    return 123

x = boring_function()

print("The boring_function has returned its result. It's:", x)





