# where the meaning of the argument is dictated by its name, not by its position
# ‒ it's called keyword argument passing.
#The position doesn't matter here ‒ each argument's value knows its
# destination on the basis of the name used
def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")

