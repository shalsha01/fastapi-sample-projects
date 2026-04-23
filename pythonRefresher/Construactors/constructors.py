# /there are two types of constructors in python
# 1. default constructor (no parameters/empty constructor)
# 2. No arguments constructor (constructor with parameters)
# 3. parameterized constructor


# defining a class with a default constructor
class Person:
    def __init__(self):
        self.name = "John Doe"
        self.age = 30

# creating an instance of the Person class using the default constructor
person1 = Person()
print("Name:", person1.name)  # Output: Name: John Doe
print("Age:", person1.age)    # Output: Age: 30


# defining a class with a parameterized constructor
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

# creating an instance of the Student class using the parameterized constructor
student1 = Student("Alice", 20, "A")
print("Name:", student1.name)   # Output: Name: Alice
print("Age:", student1.age)     # Output: Age: 20
print("Grade:", student1.grade) # Output: Grade: A

