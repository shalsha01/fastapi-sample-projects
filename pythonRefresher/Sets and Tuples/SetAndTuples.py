"""# This module provides examples and explanations of sets and tuples in Python.
    """
#     print("Index of 30:", index_of_30)
def set_and_tuple_examples():
    """
    A function that demonstrates various set and tuple operations.
    """
    # Sets
    my_set = {1, 2, 3, 4, 5}
    print("Original Set:", my_set)
    
    # Adding elements to a set
    my_set.add(6)
    print("Set after adding 6:", my_set)
    
    # Removing elements from a set
    my_set.remove(3)
    print("Set after removing 3:", my_set)
    
    # Checking membership
    is_member = 4 in my_set
    print("Is 4 in the set?", is_member)
    
    # Set operations
    another_set = {4, 5, 6, 7, 8}
    union_set = my_set.union(another_set)
    print("Union of sets:", union_set)
    
    intersection_set = my_set.intersection(another_set)
    print("Intersection of sets:", intersection_set)
    
    difference_set = my_set.difference(another_set)
    print("Difference of sets (my_set - another_set):", difference_set)
    
    # Tuples
    my_tuple = (10, 20, 30, 40, 50)
    print("Original Tuple:", my_tuple)
    
    # Accessing elements in a tuple
    first_element = my_tuple[0]
    print("First Element of Tuple:", first_element)
    
    last_element = my_tuple[-1]
    print("Last Element of Tuple:", last_element)
    
    # Tuple unpacking
    a, b, c, d, e = my_tuple
    print("Unpacked Tuple Elements:", a, b, c, d, e)
    
    # Tuples are immutable; attempting to modify will raise an error
    try:
        my_tuple[1] = 25
    except TypeError as e:
        print("Error when trying to modify a tuple:", e)
        
        
set_and_tuple_examples()    