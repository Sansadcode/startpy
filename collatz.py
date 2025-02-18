# Ask the user for a non-negative, non-zero integer
c0 = int(input("Enter a natural number: "))

# Ensure the input is valid
if c0 <= 0:
    print("Please enter a positive integer greater than zero.")
else:
    steps = 0  # Initialize step counter

    # Loop until c0 becomes 1
    while c0 != 1:
        print(c0, end=" ")  # Print the current value of c0

        # Apply Collatz rule
        if c0 % 2 == 0:
            c0 //= 2  # If even, divide by 2
        else:
            c0 = 3 * c0 + 1  # If odd, multiply by 3 and add 1

        steps += 1  # Increase step counter

    print(c0)  # Print the final value (1)
    print("Steps:", steps)  # Print total number of steps
