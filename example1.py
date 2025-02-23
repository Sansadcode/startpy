# # # lst = [[x for x in range (3)] for y in range(3)]
# # #
# # # for r in range(3):
# # #     for c in range(3):
# # #         if lst[r][c] % 2 != 0:
# # #             print("#")
# # def function_1(a):
# #     return None
# #
# #
# # # def function_2(a):
# # #     return function_1(a) * function_1(a)
# # # #
# # # # print(function_2(2))
# # # print(1 // 2)
# #
# # # def func(a, b):
# # #     return b ** a
# # #
# # # # print(func(2, 2))
# # # my_list =  [x * x for x in range(5)]
# # #
# # #
# # # def fun(lst):
# # #     del lst[lst[2]]
# # #     return lst
# # #
# # #
# # # print(fun(my_list))
# # #
# # a = 1
# # b = 0
# # a = a ^ b
# # b = a ^ b
# # a = a ^ b
# #
# # print(a, b)
# def fun(x):
#     if x % 2 == 0:
#         return 1
#     else:
#         return 2
#
#
# print(fun(fun(5)))
#
# def fun(in = 2, out = 3)
#     return in * out
#     print(fun(3))

# try:
#     first_prompt = input("enter the first vlaue")
#     a = len(first_prompt)
#     second_prompt = input("enter the second value")
#     b = len(second_prompt) * 2
#     print(a//b)
# except ZeroDivisionError:
#     print("Do not divide by zero")
# except ValueError:
#     print("wrong value")
# except:
#     print("error.error")

fruits = {'kiwi', 'cherry', 'mango','banana'}
expired_fruits = {'cherry', 'mango'}
fruits -= expired_fruits
print(fruits)