'''
Write a Python program that can do the following:
- You have $50
- You buy an item that is $15, that has a 3% tax
- Using the print()  Print how much money you have left, after purchasing the item.
'''

# solution to the assignment

my_budget = 50
item_cost = 15
tax=0.03
item_with_tax= item_cost + (item_cost * tax)
remaining_budget = my_budget - item_with_tax
print("Money left after purchase: $" + str(remaining_budget))



# End of the solution

# there is another solution to the assignment

money_left = 50 -15 - (15 * 0.03)
print("Money left after purchase: $" + str(money_left))

