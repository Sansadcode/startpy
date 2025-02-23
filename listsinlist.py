#the name of a list is the name of a memory location where the list is stored.
#The assignment: list_2 = list_1 copies the name of the array, not its contents. In effect, the two names (list_1 and list_2) identify the same location in the computer memory. Modifying
#one of them affects the other, and vice versa.
list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)

#list slice- make a brand new copy
# of a list, or parts of a list. [:]
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

