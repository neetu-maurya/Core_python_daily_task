'''1. Write a Python program to Count all letters, digits, and special

symbols from the given string

Input = “P@#yn26at^&i5ve”

Output: Chars = 8 Digits = 2 Symbol = 3'''

input_string=input("enter your string:") #input string from taken by user
#variable to define a counter
char_count=0
digit_count=0
symbol_count=0

for char in input_string:
    if char.isalpha(): #check for character
        char_count+=1
    elif char.isdigit():#check for digit
        digit_count+=1
    else:
        symbol_count+=1#check for symbol


print(f"Chars = {char_count} Digits = {digit_count} Symbols = {symbol_count}")
        
        


