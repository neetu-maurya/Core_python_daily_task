#3. Write a Python program to find duplicate values from a list and display those.

# Taking input from the user
input_string = input("Enter numbers separated by spaces: ")

# Converting the input string to a list of integers
numbers = list(map(int, input_string.split()))

# Initialize an empty set to store seen numbers and a list for duplicates
seen = set()
duplicates = []

# Iterate through the list to find duplicates
for num in numbers:
    if num in seen:
        if num not in duplicates:  # To avoid repeating the duplicates in the output
            duplicates.append(num)
    else:
        seen.add(num)

# Display the result
if duplicates:
    print("Duplicate values:", duplicates)
else:
    print("No duplicates found.")
