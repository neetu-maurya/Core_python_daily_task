5. Write a lambda function that takes one argument and returns 'Positive' if the number is
greater than 0, 'Negative' if it's less than 0, and 'Zero' if it's 0. Test it with different
numbers

# Lambda function to check if the number is positive, negative, or zero
check_number = lambda num: 'Positive' if num > 0 else 'Negative' if num < 0 else 'Zero'

# Accept input from the user
num = float(input("Enter a number: "))

# Call the lambda function and display the result
print(check_number(num))
