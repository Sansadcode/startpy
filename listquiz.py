# lst = [1, 2, 3, 4, 5]
# lst.insert(1, 6)
# del lst[0]
# lst.append(1)
#
# print(lst)
#
lst = [1, 2, 3, 4, 5]
lst_2 = []
add = 0

for number in lst:
    add += number
    lst_2.append(add)

print(lst_2)

#listwithinlist
lst = [1, [2, 3], 4]
print(lst[1])
print(len(lst))

