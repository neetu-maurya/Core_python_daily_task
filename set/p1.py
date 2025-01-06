""" 1. Write a Python program to Get Only unique items from two sets.
 Input:
 set1 = {10, 20, 30, 40, 50}
 set2 = {30, 40, 50, 60, 70}"""

# Input: Two sets from the user
set1 = set(map(int, input("Enter the elements of the first set, separated by commas: ").split(',')))
set2 = set(map(int, input("Enter the elements of the second set, separated by commas: ").split(',')))

# Combine all items from both sets while retaining shared and unique values
all_items = set1.union(set2)

# Output the result
print("Unique items from both sets:", all_items)


