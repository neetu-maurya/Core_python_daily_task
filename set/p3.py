""" 3. Write a Python program to Check if two sets have any elements in common. If
 yes, display the common elements.
 Input:
 set1 = {10, 20, 30, 40, 50}
 set2 = {60, 70, 80, 90, 10}
 Output:
 {10}"""
# Input: Two sets from the user
set1 = set(map(int, input("Enter the elements of the first set, separated by commas: ").split(',')))
set2 = set(map(int, input("Enter the elements of the second set, separated by commas: ").split(',')))

# Find common elements
common_elements = set1 & set2

# Check and display the result
if common_elements:
    print("Common elements:", common_elements)
else:
    print("No common elements found.")
