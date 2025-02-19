# Read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# We temporarily assume that the first number
# is the largest one.
# We will verify this soon.
largest_number = number1

# We check if the second number is larger than the current largest_number
# and update the largest_number if needed.
if number2 > largest_number:
    largest_number = number2

# We check if the third number is larger than the current largest_number
# and update the largest_number if needed.
if number3 > largest_number:
    largest_number = number3

# Print the result
print("The largest number is:", largest_number)
#The if-elif-else statement,
x = 10

if x == 10:  # True
    print("x == 10")

if x > 15:  # False
    print("x > 15")

elif x > 10:  # False
    print("x > 10")

elif x > 5:  # True
    print("x > 5")

else:
    print("else will not be executed")
#Nested conditional statements
    a = 10

    if a > 5:  # True
        if a == 6:  # False
            print("nested: a == 6")
        elif a == 10:  # True
            print("nested: a == 10")
        else:
            print("nested: else")
    else:
        print("else")

#comparison
a = 200
b = 53
c = 500
if a > b and c > a:
    print("both conditions are true")
a = 200
b = 33
c = 400
if a > b or a > c:
    print("at least one of the condition is true")

# nesting if condition
x = 19
if x > 10:
    print("above ten,")
    if x == 11:
         print("but not above 20")
    else:
        print("not 10")