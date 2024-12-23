''' 2. Write a Python program to get the largest and smallest number from a list without

builtin functions.'''

# Taking input from the user
input_string = input("Enter numbers separated by spaces: ")

# Converting the input string to a list of integers
numbers = list(map(int, input_string.split()))

# Initialize the first number as both the largest and smallest
largest = smallest = numbers[0]

# Loop through the list to find the largest and smallest numbers
for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

# Display the result
print("Largest number:", largest)
print("Smallest number:", smallest)
