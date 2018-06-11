def outer_function(name):
    print ("Hellow sweet little ", name)

    def inner_function():
        print (name, " you are very very little")

    return inner_function

r_function = outer_function('Giant')

print ('-'*30)

r_function()

