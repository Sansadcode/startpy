#1
def hi():
    return
    print("Hi!")
hi()
#prints none
#2
def is_int(data):
    if type(data) == int:
        return True
    elif type(data) == float:
        return False

print(is_int(5))
print(is_int(5.0))
print(is_int("5"))
#prints true, false, none
#3
def even_num_lst(ran):
    lst = []
    for num in range(ran):
        if num % 2 == 0:  #CHECKS FOR EVEN NUMBER
            lst.append(num)
    return lst

print(even_num_lst(11))
# OUTPUT [0, 2, 4, 6, 8, 10]

#4
def list_updater(lst):
    upd_list = []
    for elem in lst:
        elem **= 2
        upd_list.append(elem)
    return upd_list

foo = [1, 2, 3, 4, 5]
print(list_updater(foo))
#output - 1 4 9 16 25

#5


