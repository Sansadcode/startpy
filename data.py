# # m101 = 1
# # print(101)
# # a = 6
# # b = 3
# # a /= 2 * b
# # print(a)
# # plant = input("Enter the name of a plant: ")
# #
# # # Conditional execution
# # if plant == "Spathiphyllum":
# #     print("Yes - Spathiphyllum is the best plant ever!")
# # elif plant == "spathiphyllum":
# #     print("No, I want a big Spathiphyllum!")
# # else:
# #     print(f"Spathiphyllum! Not {plant}!")
# x = "1"
#
# if x == 1:
#     print("one")
# elif x == "1":
#     if int(x) > 1:
#         print("two")
#     elif int(x) < 1:
#         print("three")
#     else:
#         print("four")
# if int(x) == 1:
#     print("five")
# else:
#     print("six")
# i = 0
# while i < 100:
#     # do_something()
#     i += 1
# for i in range(1, 10):
#     if i % 2 == 0:
#         print(i)
# text = "OpenEDG Python Institute"
# for letter in text:
#     if letter == "I":
#         break
#     print(letter, end="")
#
# i = 0
# while i <= 3 :
#     i += 2
#     print("*")

# i = 0
# while i <= 5 :
#     i += 1
#     if i % 2 == 0:
#       break
#     print("*")
#
# for i in range(1):
#     print("#")
# else:
#     print("#")
#
# var = 0
# while var < 6:
#     var += 1
#     if var % 2 == 0:
#         continue
#     print("var""#")
#
# var = 1
# while var < 10:
#     print("#")
#     var = var << 1
my_list = [1, 2, 3, 4]
print(my_list[-3:-2])

vals = [0, 1, 2]
vals[0], vals[2] = vals[2], vals[0]
print(vals)

vals = [0, 1, 2]
vals.insert(0, 1)
del vals[1]
print(vals)

nums = [1, 2, 3]
vals = nums[-1:-2]

print(nums)
print(vals)
my_list_1 = [1, 2, 3]
my_list_2 = []
for v in my_list_1:
    my_list_2.insert(0, v)
print(my_list_2)
my_list = [1, 2, 3,]
for v in range(len(my_list)):
    my_list.insert(1, my_list[v])
print(my_list)
t = [[4-i for i in range (4)] for j in range (4)]
s = 0
for i in range(4):
    s += t[i][i]
print(s)



