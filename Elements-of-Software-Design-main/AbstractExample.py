from abc import ABC, abstractmethod
class Dog(ABC):

    def __init__(self, name, breed, height):
        self.name = name
        self.breed = breed
        self.height = height

    @abstractmethod
    def printdetails(self):
         #empty body
         pass

    def walk(selfself):
        print('I walk on 4 legs')

    @abstractmethod
    def furtype(self):
        pass


class Poodle(Dog):
    def printdetails(self):
        print("Name:", self.name)
        print("Breed:", self.breed)
        print("height:", self.height)

    def furtype(self):
        print('I have curly coat')

class GreatDane(Dog):
    def printdetails(self):
        print("Name:", self.name)
        print("Breed:", self.breed)
        print("height:", self.height)

    def furtype(self):
        print('I have short fur')


dog1 = Poodle("map", "poodle", "20")

# Call methods
dog1.printdetails()
dog1.furtype()
dog1.walk()
print()

dog2 = GreatDane("net", "greatDane", "50")

# Call methods
dog2.printdetails()
dog2.furtype()
dog2.walk()
