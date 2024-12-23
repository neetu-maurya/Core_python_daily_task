#1. Write a Python program to sum all the items in a list.

# Taking input from the user
input_string = input("Enter numbers separated by spaces: ")

# Converting the input string to a list of integers
numbers = list(map(int, input_string.split()))

# Sum all the items in the list
total_sum = sum(numbers)

# Display the result
print("Sum of all items in the list:", total_sum)


