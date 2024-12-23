''' 5. Write a Python program to traverse a given list in reverse order, and print the

elements with the original index.

Original list:

['red', 'green', 'white', 'black']

Traverse the said list in reverse order:

black

white

green

red '''
# Taking input from the user for the list
input_list = input("Enter elements of the list separated by spaces: ")

# Convert the input string into a list of strings
original_list = input_list.split()

# Traverse the list in reverse order and print the elements with their original index
print("Traverse the said list in reverse order:")
for index in range(len(original_list) - 1, -1, -1):
    print(original_list[index])
