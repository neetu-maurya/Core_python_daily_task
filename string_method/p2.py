'''2. Write a Python program to remove duplicate characters of a given

string.

Input = “String and String Function”

Output: String and Function'''

# Input string to take input from the user
input_string = input("Enter a string: ")

# Function to remove duplicate words
def remove_Duplicate(s):
    words = s.split()  # Split the string into a list of words
    seen = set()  # Set to keep track of words that have already been added
    result = []
    for word in words:
        if word.lower() not in seen:  # Case insensitive check
            seen.add(word.lower())  # Add word in lowercase to avoid case sensitivity issues
            result.append(word)  # Add the word to the result list
    return ' '.join(result)  # Join the words back into a string

# Removing duplicate words
output_string = remove_Duplicate(input_string)

# Displaying the result
print("String after removing duplicate words:", output_string)

