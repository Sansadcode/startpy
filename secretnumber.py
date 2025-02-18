# Magician's secret number
secret_number = 777

# Ask the user to enter an integer number
user_input = int(input("Enter an integer number: "))

# Continue looping until the user guesses the secret number
while user_input != secret_number:
    print("Ha ha! You're stuck in my loop!")
    user_input = int(input("Enter an integer number: "))

# When the user finally guesses correctly, print the number and the congratulatory message
print(user_input)
print("Well done, muggle! You are free now.")
