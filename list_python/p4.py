'''4. Write a Python program to split a given list into two parts where the length of the first

part of the list is given.

Original list:

[1, 1, 2, 3, 4, 4, 5, 1]

Length of the first part of the list: 3

Splitted the said list into two parts:

([1, 1, 2], [3, 4, 4, 5, 1])'''

# Taking input from the user for the list
input_list = input("Enter the elements of the list separated by spaces: ")
# Converting the input string into a list of integers
original_list = list(map(int, input_list.split()))

# Taking input from the user for the length of the first part
split_length = int(input("Enter the length of the first part of the list: "))

# Split the list into two parts
first_part = original_list[:split_length]
second_part = original_list[split_length:]

# Display the result
print("Splitted the said list into two parts:")
print(f"First part: {first_part}")
print(f"Second part: {second_part}")
