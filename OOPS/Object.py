# Constructor

# class Car:
#     def __new__(cls):
#         pass
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

# car = Car("Honda", "Civic", 2022)
# print(car.make)
# print(car.model)
# print(car.year)

# Abstraction






#Polymorphism
class shape:
    def area(self):
        return "undefined"
class rectangle(shape):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def area(self):
        return self.a*self.b
class square(shape):
    def __init__(self,a):
        self.a=a
    def area(self):
        return self.a**2
shapes=[rectangle(2,3),square(2)]
for shape in shapes:
    print(shape.area())


# Overriding polymorphism
class Animal:
    def sound(self):
        return "Some generic animal sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

Dog=Dog()
print(Dog.sound())

#Using function

def hello(animal):
    return animal.sound()
class Dog:
    def sound(self):
        return "Bark"
class Cat:
    def sound(self):
        return "Meow"
animals=[Dog(),Cat()]
for animal in animals:
    print(hello(animal))

#Inheritence

#Single Inheritance

class hello:
    def kam(self):
        return "Hello world"
class world(hello):
    def kam(self):
        return "Hello"
a=world()
print(a.kam())

#Multiple Inheritance

class animal:
    def sound(self):
        return "Hello"
class Mammals:
    def behave(self):
        return "World"
class Dog(animal,Mammals):
    def manage(self):
        return "abc"
dog=Dog()
print(dog.manage())
print(dog.behave())
print(dog.sound())

# MultiLevel Inheritance

class Animal:
    def speak(self):
        print("Animal speaks")

class Mammal(Animal):
    def has_fur(self):
        print("Mammal has fur")

class Dog(Mammal):
    def bark(self):
        print("Dog barks")

dog = Dog()
dog.speak()
dog.has_fur()
dog.bark()

#Hierrchical Inheritance

class Animal:
    def sound(self):
        return "Some generic animal sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

Dog=Dog()
print(Dog.sound())

#Hybrid Inheritance

class Animal:
    def world(self):
        return "Some generic animal sound"

class Dog(Animal):
    def hhello(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"
class Abc:
    def ding(self):
        return "Maintain"
class Cow(Animal,Abc):
    def Manage(self):
        return "Buddy"

Dog=Cat()
print(Dog.sound())
print(Dog.world())