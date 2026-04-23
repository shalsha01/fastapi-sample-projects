#Polymorphism is the ability of an object to take on many forms. In OOP, 
# it allows us to use a single interface to represent different types of objects. 
# This can be achieved through method overriding and method overloading.

class Animal:
    def speak(self):
        return "Some sound" 
class Dog(Animal):
    def speak(self):
        return "Woof!"      
class Cat(Animal):
    def speak(self):
        return "Meow!"

# Example usage
animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.speak())
    