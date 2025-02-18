print("Tell me anything...")
anything = input()
print("Hmm...", anything, "... Really?")
# Testing a TypeError message.
#thing = input("Enter a number: ")
#something = thing ** 2.0
#print(thing, "to the power of 2 is", something)
#Can you imagine how the string entered by the user flows from input() into print()
#a string: int(string)) and tries to convert it into an integer;
# a string: float(string)) and tries to convert it into a float
any = float(input("Enter a number: "))
some = any ** 2.0
print(any, "to the power of 2 is", some)
#conversions
# example refers to the earlier program to find the length of a hypotenuse. Let's run it and make it
# able to read the lengths of the legs from the console. c to the power 2 = a to the power2 + b to the power 2
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("Hypotenuse length is", hypo)
#you can remove the variable from the code.
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is", (leg_a**2 + leg_b**2) ** .5)
#string conversions
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is " + str((leg_a**2 + leg_b**2) ** .5))
#simple input
# input a float value for variable a here
leg_a = float(input("input a float value a = "))
# input a float value for variable b here
leg_b = float(input("input a float value b = "))

# output the result of addition here
print(leg_a + leg_b)
# output the result of subtraction here
print(leg_a - leg_b)
# output the result of multiplication here
print(leg_a * leg_b)
# output the result of division here
print(leg_a / leg_b)

print("\nThat's all, folks!")