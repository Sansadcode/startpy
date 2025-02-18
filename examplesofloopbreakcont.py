# Example 1
while True:
    print("Stuck in an infinite loop.")

# Example 2
counter = 5
while counter > 2:
    print(counter)
    counter -= 1

# Example 1
word = "Python"
for letter in word:
    print(letter, end="*")

# Example 2
for i in range(1, 10):
    if i % 2 == 0:
        print(i)

#example of break
text = "OpenEDG Python Institute"
for letter in text:
    if letter == "P":
        break
    print(letter, end="")

#example continue
text = "pyxpyxpyx
for letter in text:
    if letter == "x":
        continue
    print(letter, end="")

#example else in for & while
n = 0

while n != 3:
    print(n)
    n += 1
else:
    print(n, "else")

print()

for i in range(0, 3):
    print(i)
else:
    print(i, "else")
#example of range
for i in range(3):
    print(i, end=" ")  # Outputs: 0 1 2

for i in range(6, 1, -2):
    print(i, end=" ")  # Outputs: 6, 4, 2
#quiz sample scripts
#1 print odd num
for i in range(0, 11):
    if i % 2 != 0:
        print(i)
#2 print odd numb while
x = 1
while x < 11:
    if x % 2 != 0:
        print(x)
    x += 1
#3.for loop and a break statement. The program should iterate over characters
# in an email address, exit the loop when it reaches the # @ symbol,
# and print the part before @ on one line.
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")
#4.for loop and a continue statement. The program should iterate over a string
# of digits, # replace each 0 with x, and print the modified string to the screen
for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")
#