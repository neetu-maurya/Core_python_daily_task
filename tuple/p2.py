"""
2.Write a Python program to convert a list to a tuple.
 Input: listx = [5, 10, 7, 4, 15, 3]
 Output: (5, 10, 7, 4, 15, 3)"""

# Input: List elements from the user
user_input = input("Enter the elements of the list, separated by commas: ")

# Convert the input string to a list of integers
listx = list(map(int, user_input.split(',')))

# Convert the list to a tuple
tuplex = tuple(listx)

# Output the tuple
print("Tuple:", tuplex)
