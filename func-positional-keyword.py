def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)
adding(c = 1, a = 2, b = 3)
adding(3, c = 1, b = 2) #the arguments for c and b are specified as keyword ones.
adding(3, a = 1, b = 2)#TypeError: adding() got multiple values for argument 'a'
adding(4, 3, c = 2) #mixing




