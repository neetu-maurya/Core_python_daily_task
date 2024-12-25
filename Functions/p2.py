2. Declare a square() function with one parameter.Then call the function and pass one
number and display the square of that number .

#square function
def square(number1):
    result=number1*number1
    print("Square of number is:",result)
#input function
num1=int(input("enter a number which you want to calculate the square:"))
#call the function
square(num1)
