# my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# repeat = [1, 2, 4,]
# new_list = 0
# # Write your code here.
# for i in range(len(my_list)):
#     if i in repeat:
#         new_list += 1
#         print("The list with unique elements only:")
# print(my_list)
# def remove_duplicates(input_list):
#     # Convert the list to a set to remove duplicates, then convert it back to a list
#     return list(set(input_list))
#
# # Example usage
# numbers = [1, 2, 3, 2, 4, 5, 1, 6, 4]
# unique_numbers = remove_duplicates(numbers)
#
# print("List after removing duplicates:", unique_numbers)
# Original list with duplicates
numbers = [1, 2, 3, 2, 4, 5, 1, 6, 4]

# Remove duplicates by converting the list to a set and then back to a list
numbers = list(set(numbers))

# Print the result
print("List after removing duplicates:", numbers)
