# 2. Python Program to Find the Largest Among Three Numbers

#input function to take the input from user

number1=int(input("enter the first number:"))
number2=int(input("enter the second number:"))
number3=int(input("enter the third number:"))

#condition to check the largest number

if (number1>number2)and (number1>number3):
    print(f'{number1} is largest number')

elif (number2>number1) and (number2>number3):
    print(f'{number2} is largest number')

else:
    print(f'{number3} is largest number')
