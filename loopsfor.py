# Read three numbers.
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# Check which one of the numbers is the greatest
# and pass it to the largest_number variable.

largest_number = max(number1, number2, number3)

# Print the result.
print("The largest number is:", largest_number)

def find_largest_of_ten(numbers):
    largest = numbers[0]  # Assume the first number is the largest

    for num in numbers[1:]:  # Compare with the remaining numbers
        if num > largest:
            largest = num

    return largest

# Taking 10 numbers as input
numbers = [float(input(f"Enter number {i+1}: ")) for i in range(10)]

print("The largest number is:", find_largest_of_ten(numbers))