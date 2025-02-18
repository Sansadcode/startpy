my_list = []

num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = float(input("Enter a list element: "))
    my_list.append(val)

# Using the built-in sort method
my_list.sort()

print("\nSorted:")
print(my_list)