#a variable existing outside a function has scope inside the function's body.
def my_function():
    var = 2
    print("Do I know that variable?", var)
var = 1
my_function()
print(var)
#A variable existing outside a function
# has scope inside the function's body, excluding those which define a
# variable of the same name.
#t also means that the scope of a variable existing outside a function
# is supported only when getting # its value (reading). Assigning a value forces
# the creation of the function's own variable.
def my_function():
    var = 2
    print("Do I know that variable?", var)
var = 1
my_function()
print(var)

#extend a variable's scope in a way which includes the function's body
# (even if you want not only to read the values, but also to modify them).
#Such an effect is caused by a keyword named global:
def my_function():
    global var
    var = 2
    print("Do I know that variable?", var)
var = 1
my_function()
print(var)

#1
var = 2


def mult_by_var(x):
    return x * var
print(mult_by_var(7))    # outputs: 14
#2
def mult(x):
    var = 5
    return x * var
print(mult(7))    # outputs: 35
#3
def mult(x):
    var = 7
    return x * var
var = 3
print(mult(7))    # outputs: 49
#4
def adding(x):
    var = 7
    return x + var
print(adding(4))    # outputs: 11
print(var)    # NameError
#5
var = 2
print(var)    # outputs: 2
def return_var():
    global var
    var = 5
    return var
print(return_var())    # outputs: 5
print(var)    # outputs: 5











