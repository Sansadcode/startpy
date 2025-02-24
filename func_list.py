def list_sum(lst):
    s = 0

    for elem in lst:
        s += elem

    return s

print(list_sum([5, 4, 3]))

#Any entity recognizable by Python can be a function result.
def strange_list_fun(n):
    strange_list = []

    for i in range(0, n):
        strange_list.insert(0, i)

    return strange_list
print(strange_list_fun(5))



def function(x=0):
    return x
print(function())

def f(x):
    if x == 0:
        return 0
    return x + f(x - 1)


print(f(3))
def fun(x):
    x += 1
    return x


x = 2
x = fun(x + 1)
print(x)

################
def func_1(a):
    return a ** a


def func_2(a):
    return func_1(a) * func_1(a)


print(func_2(2))

# def fun(x):
#     if x % 2 == 0:
#         return 1
#     else:
#         return
#
#
# print(fun(fun(2)) + 1)

def fun(x):
    global y
    y = x * x
    return y
fun(2)
print(y)


def fun(x, y, z):
    return x + 2 * y + 3 * z

print(fun(0, z=1, y=3))

def fun(inp=2, out=3):
    return inp * out


print(fun(out=2))
tup = (1, 2, 4, 8)
tup = tup[1:-1]
tup = tup[0]
print(tup)




x = 1
y = 2
x, y, z = x, x, y
z, y, z = x, y, z

print(x, y, z)
#
# a = 1
# b = 0
# a = a ^ b
# b = a ^ b
# a = a ^ b
#
# print(a, b)
# nums = [1, 2, 3]
# vals = nums
# del vals[:]
# print(vals)
#
#
# x = int(input())
# y = int(input())
# x = x % y
# x = x % y
# y = y % x
# print(y)
#
# y = input()
# x = input()
# print(x + y)
def fun(x, y):
    if x == y:
        return x
    else:
        return fun(x, y-1)

print(fun(0, 4))

