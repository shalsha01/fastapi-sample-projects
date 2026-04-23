# inheritance is a powerful feature in object-oriented programming that allows a new class (called a child or subclass) 
# to inherit properties and behaviors from an existing class (called a parent or superclass). 
# This promotes code reusability and establishes a natural hierarchical relationship between classes.

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"
    
class Dog(Animal): # the dog class inherits from the animal class
    def speak(self):
        return "Woof!"

class Cat(Animal): # the cat class inherits from the animal class
    def speak(self):
        return "Meow!"

# Example usage
dog = Dog("Buddy")
cat = Cat("Whiskers")
print(f"{dog.name} says: {dog.speak()}")  # Output: Buddy says: Woof!
print(f"{cat.name} says: {cat.speak()}")  # Output: Whiskers says: Meow!


