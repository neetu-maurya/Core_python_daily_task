# Taking input from the user
input_string = input("Enter a string: ")

# Splitting the string into a list of words, reversing the list, and joining back
reversed_words = " ".join(input_string.split()[::-1])

# Displaying the result
print("Reversed Words String:", reversed_words)

