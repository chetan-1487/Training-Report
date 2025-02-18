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

#Inheritence