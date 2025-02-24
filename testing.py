# # my_dict = {'1': "2", '3': "3"}
# # my_dict.get('1')
# # print(my_dict)
# # return
# # print([1,2,3] + [4,5])
# # print(bool([]))
# # print({1: 'one', 2:'two'}[3]
# # my_list = [4, 3, 2, 1]
# # print(my_list[3:5])
# the_data = ['data', -1, 2.7183949]
# print(the_data.index(-1) > 0)
# print('data' in the_data)
# print(int(the_data[2]) == len(the_data))
# print(the_data[1] not in the_data)

def combine(width, height=10, depth=0, is_3D=False):
    return[is_3D, width, height, depth]
print(combine(height = 1, width =2)[3])

def walk(top):
         if top == 0:
             return 0
         return top + walk(top - 1)
print(walk(2))