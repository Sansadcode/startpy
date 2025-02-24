#define BMI
def bmi(weight, height):
    return weight / height ** 2
print(bmi(52.5, 1.65))

#check them both and return None if any of them looks suspicious.
#take a look at the way the backslash (\) symbol is used. If you use it in
# Python code and end a line with it,# it will tell Python to continue the
# line of code in the next line of code.
def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200:
        return None
    return weight / height ** 2
print(bmi(352.5, 1.65))

#convert imperial units to metric ones.1 lb = 0.45359237 kg
def lb_to_kg(lb):
    return lb * 0.45359237
print(lb_to_kg(1))
#feet and inches: 1 ft = 0.3048 m, and 1 in = 2.54 cm = 0.0254 m.
def ft_and_inch_to_m(ft, inch):
    return ft * 0.3048 + inch * 0.0254
print(ft_and_inch_to_m(1, 1))

# feet without inches
def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254
print(ft_and_inch_to_m(6))

#finalcode
def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254
def lb_to_kg(lb):
    return lb * 0.4535923
def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None
    return weight / height ** 2
print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7)))
