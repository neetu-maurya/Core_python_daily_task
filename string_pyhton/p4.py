# Input string to take input from user
input_string=input('Enter sentence for count the vowels:')


# Define vowels
vowels = "aeiouAEIOU"

# Initialize a count variable
vowel_count = 0

# Initialize an empty list to store vowels found
found_vowels = []

# Iterate through each character in the string
for char in input_string:
    if char in vowels:
        vowel_count += 1
        found_vowels.append(char)

# Display the result
print("Original String:", input_string)
print("Number of vowels:", vowel_count)
print("Vowels found:", ", ".join(found_vowels))
