#positional argument passing in which the order of arguments passed matters (Ex. 1)
def subtra(a, b):
    print(a - b)

subtra(5, 2)    # outputs: 3
subtra(2, 5)    # outputs: -3


#keyword (named) argument passing in which the order of arguments passed doesn't matter (Ex. 2)Ex. 2
def subtra(a, b):
    print(a - b)

subtra(a=5, b=2)    # outputs: 3
subtra(b=2, a=5)    # outputs: 3

#a mix of positional and keyword argument passing (Ex. 3.)
def subtra(a, b):
    print(a - b)

subtra(5, b=2)    # outputs: 3
subtra(5, 2)    # outputs: 3

#example snippets
def intro(a="James Bond", b="Bond"):
    print("My name is", b + ".", a + ".")
intro()

#2
def intro(a="James Bond", b="Bond"):
    print("My name is", b + ".", a + ".")

intro(b="Sean Connery")
#3
def intro(a, b="Bond"):
    print("My name is", b + ".", a + ".")

intro("Susan")

#4 SyntaxError - a non-default argument (c) follows a default argument (b=2).
def add_numbers(a, b=2, c):
    print(a + b + c)

add_numbers(a=1, c=3)



