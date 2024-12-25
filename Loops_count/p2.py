#2. Python program to check if the given string is a palindrome

# Function to check if a string is a palindrome
def is_palindrome(string):
    # Remove spaces and convert to lowercase for uniformity
    string = string.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return string == string[::-1]

# Taking user input
text = input("Enter a string: ")

# Check and display result
if is_palindrome(text):
    print(f'"{text}" is a palindrome.')
else:
    print(f'"{text}" is not a palindrome.')
