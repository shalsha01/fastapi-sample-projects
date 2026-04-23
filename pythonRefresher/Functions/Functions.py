"""This module provides examples and explanations of functions in Python.
    """
    
def greet(first_name, last_name):
    """Greets a person with their name."""
    return f"Hello,{first_name} {last_name}!"

def add(a, b):
    """Returns the sum of two numbers."""
    print (a+b)


print(greet("shahd", " haider "))
add(5, 3)



def buy_item(cost_of_item):
    return cost_of_item + add_tax_to_item(cost_of_item) 

def add_tax_to_item(cost_of_item):
    current_tax_rate = 0.07
    return cost_of_item * current_tax_rate

final_cost = buy_item(100)

print(final_cost)