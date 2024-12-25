Q.2) Using input function take two number and then swap the number

# Taking two numbers as input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(f"Before swapping: num1 = {num1}, num2 = {num2}")

# Swapping the numbers
num1, num2 = num2, num1

print(f"After swapping: num1 = {num1}, num2 = {num2}")
