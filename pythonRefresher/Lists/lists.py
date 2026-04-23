'''
this module contains examples and functions related to Python lists.
'''
my_list = [45, 37, 100,89, 5, 67]
print("Original List:", my_list)
# Accessing elements
first_element = my_list[0]
print("First Element:", first_element)
last_element = my_list[-1]
print("Last Element:", last_element)
# Slicing
sub_list = my_list[1:4]
print("Sub List (index 1 to 3):", sub_list)
# Modifying elements
my_list[2] = 150
print("Modified List:", my_list)
# Appending elements
my_list.append(200)
print("List after appending 200:", my_list)
# Removing elements
my_list.remove(89)
print("List after removing 89:", my_list)
# Iterating through the list
print("Iterating through the list:")
for item in my_list:
    print(item)
# List length
list_length = len(my_list)
print("Length of the List:", list_length)
# Sorting the list
my_list.sort()
print("Sorted List:", my_list)
# Reversing the list
my_list.reverse()
print("Reversed List:", my_list)
# List comprehension
squared_list = [x**2 for x in my_list]
print("Squared List using List Comprehension:", squared_list)
# Nested lists
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Nested List:", nested_list)
first_nested_element = nested_list[0][1]
print("First element of the first nested list:", first_nested_element)
def list_operations_example():
    '''
    A function that demonstrates various list operations.
    '''
    sample_list = [10, 20, 30, 40, 50]
    print("Sample List:", sample_list)
    
    # Adding an element
    sample_list.append(60)
    print("After appending 60:", sample_list)
    
    # Removing an element
    sample_list.remove(20)
    print("After removing 20:", sample_list)
    
    # Finding the index of an element
    index_of_30 = sample_list.index(30)
    print("Index of 30:", index_of_30)
    
    # Counting occurrences of an element
    count_of_10 = sample_list.count(10)
    print("Count of 10:", count_of_10)
    
    # Popping the last element pop method removes and returns the last item(index -1) from the list
    sample_list.pop()
    
    # Clearing the list
    sample_list.clear()
    print("After clearing the list:", sample_list)
# Call the function to demonstrate list operations
list_operations_example()
# Output:
# Original List: [45, 37, 100, 89, 5, 67]
# First Element: 45 
# Last Element: 67
# Sub List (index 1 to 3): [37, 100, 89]
# Modified List: [45, 37, 150, 89, 5, 67]
# List after appending 200: [45, 37, 150, 89, 5, 67, 200]
# List after removing 89: [45, 37, 150, 5, 67, 200]
# Iterating through the list:
# 45
# 37
# 150
# 5
# 67
# 200
# Length of the List: 6
# Sorted List: [5, 37, 45, 67, 150, 200]
# Reversed List: [200, 150, 67, 45, 37, 5]
# Squared List using List Comprehension: [40000, 22500, 4489, 2025, 1369, 25]
# Nested List: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# First element of the first nested list: 2
# Sample List: [10, 20, 30, 40, 50]
# After appending 60: [10, 20, 30, 40, 50, 60]
# After removing 20: [10, 30, 40, 50, 60]
# Index of 30: 1
# Count of 10: 1
# After clearing the list: []
# Note: The output comments are for illustrative purposes and will not be printed when the code is run.