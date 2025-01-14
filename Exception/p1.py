"""1. Write a Python program to handle a ZeroDivisionError exception when dividing a

number by zero."""


try:
     # Get input from the user
    numerator=int(input("enter a numerator number:"))
    denominator=int(input("enter a denominator number:"))
     # Perform division
    result=numerator/denominator
    print(f" {numerator} / {denominator} = {result}")

except ZeroDivisionError:
     # Handle division by zero
    print("Error:Cannot divide by zero. Please provide a non-zero denominator.")
    

