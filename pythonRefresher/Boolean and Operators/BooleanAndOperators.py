"""This module provides a refresher on Boolean values and operators in Python.
    """
    
def boolean_examples():
    """
    A function that demonstrates various Boolean operations.
    """
    # Boolean values
    true_value = True
    false_value = False
    print("Boolean True:", true_value)
    print("Boolean False:", false_value)
    
    # Comparison operators
    a = 10
    b = 20
    print("Is a equal to b?", a == b)
    print("Is a not equal to b?", a != b)
    print("Is a less than b?", a < b)
    print("Is a greater than or equal to b?", a >= b)
    
    # Logical operators
    print("Logical AND (True and False):", True and False)
    print("Logical OR (True or False):", True or False)
    print("Logical NOT (not True):", not True)
    
    # Combining comparisons with logical operators
    x = 15
    print("Is x between 10 and 20?", (x > 10) and (x < 20))
    print("Is x less than 10 or greater than 20?", (x < 10) or (x > 20))
    
    # Boolean conversion
    print("Boolean value of 0:", bool(0))
    print("Boolean value of non-zero number (5):", bool(5))
    print("Boolean value of empty string:", bool(""))
    print("Boolean value of non-empty string ('Hello'):", bool("Hello"))
    
boolean_examples()




