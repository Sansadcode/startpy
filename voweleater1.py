# Ask the user to enter a word
user_word = input("Enter a word: ")

# Convert the word to upper case
user_word = user_word.upper()

# Initialize an empty string to store the word without vowels
word_without_vowels = ""

# Loop over each letter in the word
for letter in user_word:
    # Check if the letter is a vowel; if so, skip it
    if letter in ('A', 'E', 'I', 'O', 'U'):
        continue
    # Concatenate non-vowel letters to the new string
    word_without_vowels += letter

# Print the final word without vowels
print("Word without vowels:", word_without_vowels)
