#Write a Python program to find the number of times 4 appears in the tuple.

# Input tuple from the user
user_input = input("Enter the elements of the tuple, separated by commas: ")

# Convert the input string to a tuple
numbers = tuple(map(int, user_input.split(',')))

# Count the occurrences of the number 4
count_of_fours = numbers.count(4)

# Print the result
print(f"The number 4 appears {count_of_fours} times in the tuple.")

