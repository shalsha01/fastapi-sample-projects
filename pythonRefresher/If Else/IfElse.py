"""# This script demonstrates the use of if, elif, and else statements in Python.
    """
    
# Define a variable with a numeric value
number = 10
# Check if the number is positive, negative, or zero

if number > 0:
    print(f"{number} is a positive number.")
elif number < 0:
    print(f"{number} is a negative number.")
else:
    print("The number is zero.")
    
# Define another variable with a string value
color = "red"
# Check the value of the color variable
if color == "red":
    print("The color is red.")
elif color == "blue":
    print("The color is blue.")
else:
    print("The color is neither red nor blue.")
    
# Define a variable with an age value
age = 25
# Check the age category
if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")

        