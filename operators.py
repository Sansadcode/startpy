kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 3.4
kilometers_to_miles = kilometers / 3.4


print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

# Take a look at the code in the editor: it reads a float value, puts
# it into a variable named x, and prints the value of a variable named y.
# Your task is to complete the code in order to evaluate the following expression:
#3x3 - 2x2 + 3x - 1
#The result should be assigned to y.
x = 0
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

x = 1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

x = -1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)
#Your task is to complete the code in order to evaluate the following expression:
#
x = float(input("Enter value for x: "))
y = 1./(x + 1./(x + 1./(x + 1./x)))
print("y =", y)
