# Ask the user to enter a word
user_word = input("Enter a word: ")

# Convert the word to upper case
user_word = user_word.upper()
print(user_word)
# Loop over each letter in the word
for letter in user_word:
    # If the letter is a vowel, skip printing it
    if letter == 'A':
        continue
    elif letter == 'E':
        continue
    elif letter == 'I':
        continue
    elif letter == 'O':
        continue
    elif letter == 'U':
        continue
    else:
        # Print each non-vowel letter on a separate line
        print(letter)
