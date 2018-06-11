def func1():
    name = 'Name'
    num1 = 23
    num2 = 56

    def func2():
        print (name + str(num1) + str(num2))

    return func2

c = func1()

print (c.__closure__)

print (c.__closure__[0].cell_contents)
print (c.__closure__[1].cell_contents)
print (c.__closure__[2].cell_contents)

