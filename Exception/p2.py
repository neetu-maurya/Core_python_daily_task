"""2. Write a Python program that prompts the user to input an integer and raises a

ValueError exception if the input is not a valid integer."""

#taking user input
try:
     
    numerator=int(input("enter a numerator:"))
    denominator=int(input("enter denominator:"))
    #storing the result
    result=numerator/denominator
    print(f"{numerator}/{denominator} = {result}")

except ValueError:
    #handle value type exception
    print("Error :enter a valid number")
except ZeroDivisionError:
    #handle zero division error
    print("Error : zero can not divisible change the denominator value")
    

          

              

