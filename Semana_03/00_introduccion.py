class Cat:
    def __init__(self, name):
        self.__name = name
    def __str__(self):
        return f'Cat with name {self.__name}.'

#cat = Cat('Archie')
#print(cat) # str() is called inside the print()

class Cat:
    def __init__(self, name = 'Leo', age = 5):
        self.__name = name 
        self.__age = age

    def __str__(self):
        return f'Cat {self.__name}'

    def __repr__(self):
        return f'Cat {self.__age}'

littleCat = Cat('Bella', 2)
bigCat = Cat('Charlie', 12)
print('str():')
print(littleCat)
print(bigCat)
print('repr():')
print(repr(littleCat))
print(repr(bigCat))