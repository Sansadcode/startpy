# Write a program that utilizes the concept of conditional execution, takes a string as input, and:
# prints the sentence "Yes - Spathiphyllum is the best
# plant ever!" to the screen if the inputted string is "Spathiphyllum" (upper-case)
# prints "No, I want a big Spathiphyllum!" if the inputted string is "spathiphyllum" (lower-case)
# prints "Spathiphyllum! Not [input]!" otherwise. Note: [input] is the string taken as input.
# Test your code using the data we've provided for you. And get yourself a Spathiphyllum, too!

plant = input("enter the plant name:")

if plant == "Spathiphyllum":
    print("yes spathiphyllum is the best plant ever")
elif plant != "Spathiphyllum":
    print(f"Spathiphyllum not {plant} ")
else:
    print("no,I want a big Spathiphyllum")
