numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)
###
numbers.append(4)
print(len(numbers))
print(numbers)
###

numbers.insert(0, 222)
print(len(numbers))
print(numbers)
numbers.insert(1, 333)

my_list = []  # Creating an empty list.

for i in range(5):
    my_list.append(i + 1)

print(my_list)

mynew_list = []  # Creating an empty list.

for i in range(5):
    mynew_list.insert(0, i + 1)

print(mynew_list)