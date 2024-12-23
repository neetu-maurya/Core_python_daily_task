'''4. Write a Python Count vowels in a string

input= “Welcome to Python Assig'''

# Input string to take input from user
input_string = input("Enter a string: ")

# Define vowels
vowels = "aeiouAEIOU"

# Initialize a counter for vowels
vowel_count = 0

# Iterate through each character in the string
for char in input_string:
    if char in vowels:  # Check if the character is a vowel
        vowel_count += 1

# Display the result
print("Number of vowels:", vowel_count)
