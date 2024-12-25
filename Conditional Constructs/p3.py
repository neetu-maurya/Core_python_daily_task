#3. Python Program to Check if a Number is Positive, Negative or 0

#input from the user

number=int(input("enter any number to check the number is positive,negative,or zero:"))

#condition for checking number

if number>0:
    print(f'{number}  is a positive number')
elif number<0:
    print(f'{number}  is a negative number')

else:
    print(f'{number}  is a zero number')
