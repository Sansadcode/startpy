#A tuple is an immutable sequence type. It can behave like a list, but it can't be modified
#tuples prefer to use parenthesis,
# it's also possible to create a tuple just from a set of values separated by commas.
tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125

print(tuple_1)
print(tuple_2)

#
my_tuple = (1, 10, 100, 1000)
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:
    print(elem)
    #output 1 # 1000 # (10, 100, 1000)  # (1, 10) #1 # 10 # 100 # 1000
# the below code will give attribute error as tuples cannot be modified
my_tuple = (1, 10, 100, 1000)

my_tuple.append(10000)
del my_tuple[0]
my_tuple[1] = -10

#other built in functions to use with tuple
my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000) #the + operator can join tuples together
t2 = my_tuple * 3 #the * operator can multiply tuples, just like lists

print(len(t2))  #returns the number of elements contained inside
print(t1)
print(t2)
print(10 in my_tuple) #the in and not in operators work in the same way as in lists.
print(-10 not in my_tuple)

#useful tuple properties is their ability to appear on the left side of the assignment operator.
var = 123

t1 = (1, )
t2 = (2, )
t3 = (3, var)

t1, t2, t3 = t2, t3, t1

print(t1, t2, t3)

#It shows three tuples interacting − in effect, the values stored in them
# "circulate" − t1 becomes t2, t2 becomes t3, and t3 becomes t1.
#Note: the example presents one more important fact: a tuple's elements can be variables,
# not only literals. Moreover, they can be expressions if they're on the right side of the
# assignment operator.