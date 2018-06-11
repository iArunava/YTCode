class Person:
    has_legs = True
    this_is_a_data = 'Someone rightly said naming variables is the most difficult part of programming'

    __hotel_I_stayed_last_night = "can't share"
    __something_else_nonpublic_to_me = 'nonpublic stuff'

    def __init__(self, weight, height, myphn):
        self.weight = weight
        self.height = height
        self.__myphn = myphn

    def this_is_a_func(self):
        print ('A print from a public method in Person class')

    def __nonpublic_method(self):
        print ('Hey this is a nonpublic method accessible only from inside the class')

    # getter
    def get_has_legs(self):
        return self.has_legs

    # setter
    def set_has_legs(self, value):
        if type(value) == bool:
            self.has_legs = value
        else:
            raise Exception ('Unknown value passed!')

d1 = Person(23, 56, 1002220)

print (d1._Person__hotel_I_stayed_last_night)
print (d1._Person__something_else_nonpublic_to_me)
d1._Person__nonpublic_method()
print (Person._Person__hotel_I_stayed_last_night)
print (Person._Person__something_else_nonpublic_to_me)

