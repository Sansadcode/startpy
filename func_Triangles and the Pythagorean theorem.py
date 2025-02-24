def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b
a = float(input('Enter the first side\'s length: '))
b = float(input('Enter the second side\'s length: '))
c = float(input('Enter the third side\'s length: '))

if is_a_triangle(a, b, c):
    print('Yes, it can be a triangle.')
else:
    print('No, it can\'t be a triangle.')

#In the second step, we'll try to ensure that a certain triangle is a right-angle triangle.
# We will need to make use of the Pythagorean theorem:c2 = a2 + b2
# How do we recognize which of the three sides is the hypotenuse?
# The hypotenuse is the longest side.
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b
def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
print(is_a_right_triangle(5, 3, 4))
print(is_a_right_triangle(1, 3, 4))



