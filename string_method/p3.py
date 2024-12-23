'''3. Write a Python program to count Uppercase, Lowercase, special

character and numeric values in a given string

Input = “Hell0 W0rld ! 123 * # welcome to pYtHoN”

Output:

UpperCase : 5

LowerCase : 18

NumberCase : 5

SpecialCase : 11 '''

# Input string to take input from user
input_string = input("Enter a string: ")

# Initialize counters
upper_case_count = 0
lower_case_count = 0
digit_count = 0
special_char_count = 0

# Iterate through each character in the string
for char in input_string:
    if char.isupper():  # Check if the character is uppercase
        upper_case_count += 1
    elif char.islower():  # Check if the character is lowercase
        lower_case_count += 1
    elif char.isdigit():  # Check if the character is a digit
        digit_count += 1
    else:  # If it's neither uppercase, lowercase, nor a digit, it's a special character
        special_char_count += 1

# Display the results
print("UpperCase:", upper_case_count)
print("LowerCase:", lower_case_count)
print("NumberCase:", digit_count)
print("SpecialCase:", special_char_count)
