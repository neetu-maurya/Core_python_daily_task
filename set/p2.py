"""2. Write a Python program to Return a set of elements present in Set A or B, but
 not both.
 Input:
 set1 = {10, 20, 30, 40, 50}
 set2 = {30, 40, 50, 60, 70}
 Output:
 {20, 70, 10, 60}"""

# Input: Two sets from the user
set1 = set(map(int, input("Enter the elements of the first set, separated by commas: ").split(',')))
set2 = set(map(int, input("Enter the elements of the second set, separated by commas: ").split(',')))

# Get only unique items from both sets using symmetric difference
unique_items = set1 ^ set2

# Output the result
print("Unique items from both sets:", unique_items)

