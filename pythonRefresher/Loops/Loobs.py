"""# This script demonstrates the use of loops in Python.
    """
    
# Using a for loop to iterate over a list of numbers
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(f"Number: {num}")
    
# Using a while loop to print numbers from 1 to 5
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1

# Using a for loop with range to print even numbers from 0 to 10
for i in range(0, 11, 2):
    print(f"Even Number: {i}")

# Using a while loop to calculate the sum of numbers from 1 to 10
total = 0
num = 1
while num <= 10:
    total += num
    num += 1
print(f"Total Sum from 1 to 10: {total}")


# Using a for loop to iterate over a string
message = "Hello"
for char in message:
    print(f"Character: {char}")
# Using a while loop to reverse a string
original = "Python"
reversed_str = ""
index = len(original) - 1
while index >= 0:
    reversed_str += original[index]
    index -= 1
print(f"Reversed String: {reversed_str}")

# Using a for loop with break statement
for i in range(1, 11):
    if i == 6:
        print("Breaking the loop at 6")
        break
    print(f"Number before break: {i}")
# Using a while loop with continue statement
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue
    print(f"Odd Number: {count}")
# Nested loops example
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i: {i}, j: {j}")
        
