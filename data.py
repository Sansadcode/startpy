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
text = "OpenEDG Python Institute"
for letter in text:
    if letter == "I":
        break
    print(letter, end="")