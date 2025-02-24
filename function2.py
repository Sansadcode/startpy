def introduction(first_name, last_name="Smith"):
    print("Hello, my name is", first_name, last_name)
introduction("James", "Doe")
introduction(first_name="William")#If you use one keyword argument, the remaining one will take the default value:
introduction("Henry")

def address(street, city, postal_code):
    print("Your address is:", street, "St.,", city, postal_code)
#An example of a three-parameter function:
s = input("Street: ")
p_c = input("Postal Code: ")
c = input("City: ")
address(s, c, p_c)

