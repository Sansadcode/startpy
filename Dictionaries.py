#The dictionary is another Python data structure. It's # not a sequence type
# (but can be easily adapted to sequence processing) and it is mutable.
#The list of pairs is surrounded by curly braces, while the pairs
# themselves are separated by commas, and the keys and values by colons.

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)
# Print the values here.
print(dictionary['cat'])
print(phone_numbers['Suzy']) #keys are case-sensitive: 'Suzy' is something different from 'suzy'.


#mustn't use a non-existent key
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
words = ['cat', 'lion', 'horse']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")


#for loops in dictionaries method keys()
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for key in dictionary.keys(): #  returns an iterable object consisting of all the keys gathered within the dictionary.
    print(key, "->", dictionary[key])

#items() returns tuples where each tuple is a key-value pair.
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for english, french in dictionary.items():
    print(english, "->", french)

#replacing values
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary['cat'] = 'minou'
print(dictionary)
#sorted
# for key in sorted(dictionary.keys()):

#values() method
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for french in dictionary.values():
    print(french)

#adding a new key value pair
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary['swan'] = 'cygne'
print(dictionary)

# insert an item to dictionary using update()
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary.update({"duck": "canard"})
print(dictionary)

#removing an item from dictionary
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

del dictionary['dog']
print(dictionary)

#to remove last item popitem()
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary.popitem()
print(dictionary)    # outputs: {'cat': 'chat', 'dog': 'chien'}








