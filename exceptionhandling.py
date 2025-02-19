#define the function name and input value.
def divide_by_five(number):
    try:
        value = 5 / number
    except ZeroDivisionError:  #exception handler
        print('divided by zero')
        value = 1
        #giving this value is important as it will return the value if not gives error
    return value
print(divide_by_five(2))
print(divide_by_five(0))
