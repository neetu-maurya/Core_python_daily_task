"""3.create a program to accept choice from user and perform the operation according

	a. Try except

	b. try multiple except

	c. try except else

	d. finally

	e. try single except

	f. raising exception """

#try except
def try_Except():
    try:
        numerator=int(input("enter a numerator:"))
        denominator=int(input("enter denominator:"))
    #storing the result
        result=numerator/denominator
        print(f"{numerator}/{denominator} = {result}")

    except ValueError:
        #handle value type exception
        print("Error :enter a valid number")
        
    
    
#try multiple except

def try_Multiple_Except():
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

#try except else

def try_except_Else():
     try:
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        result = numerator / denominator
     except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
     else:
        print(f"The result is: {result}")
        
#finally

def finally_try_except():
    try:
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        result = numerator / denominator
        print(f"The result is: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    finally:
        print("Execution completed, with or without an error.")
# try single except
def try_Single_Except():
    try:
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        result = numerator / denominator
        print(f"The result is: {result}")
    except Exception as e:
        print(f"An error occurred: {e}")
#  raising exception

def raising_Exception():
    try:
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        if denominator == 0:
            raise ZeroDivisionError("You cannot divide by zero.")
        result = numerator / denominator
        print(f"The result is: {result}")
    except ZeroDivisionError as e:
        print(f"Raised Exception: {e}")

def main():
    print("Choose an option to demonstrate exception handling:")
    print("1. Try Except")
    print("2. Try Multiple Except")
    print("3. Try Except Else")
    print("4. Finally")
    print("5. Single Except")
    print("6. Raising Exception")
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        try_Except()
    elif choice == '2':
        try_Multiple_Except()
    elif choice == '3':
        try_except_Else()
    elif choice == '4':
        finally_try_except()
    elif choice == '5':
        try_Single_Except()
    elif choice == '6':
        raising_Exception()
    else:
        print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

       
    
    
