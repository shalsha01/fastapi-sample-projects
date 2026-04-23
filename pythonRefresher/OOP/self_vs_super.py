# self vs super are two important concepts in OOP that are used to refer to the current instance of a class and the parent class, respectively.

class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, I am {self.name} from the Parent class."
    
class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Call the constructor of the Parent class
        self.age = age

    def greet(self):
        parent_greeting = super().greet()  # Call the greet method of the Parent class
        return f"{parent_greeting} I am {self.age} years old from the Child class."
    
# Example usage
child = Child("Alice", 10)
print(child.greet())
