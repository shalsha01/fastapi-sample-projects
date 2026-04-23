# for formatin strings in python we have multiple ways to do that
name = "Shahad"
age = 24        
# 1. using concatenation    
print("My name is: " + name + " and I am: " + str(age) + " years old.")
# 2. using f-strings (formatted string literals)
print(f"My name is: {name} and I am: {age} years old.")
# 3. using the format() method
print("My name is: {} and I am: {} years old.".format(name, age))
# 4. using %-formatting
print("My name is: %s and I am: %d years old." % (name, age))
# 5. using template strings from the string module

from string import Template
template = Template("My name is: $name and I am: $age years old.")
print(template.substitute(name=name, age=age))
# All of these methods will output the same result:

# My name is: Shahad and I am: 24 years old.
