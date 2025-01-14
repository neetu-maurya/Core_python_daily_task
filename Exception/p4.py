

def get_numbers():
    try:
        # Get input from the user
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")
        
        # Check if inputs are numeric
        if not (num1.replace('.', '', 1).isdigit() and num2.replace('.', '', 1).isdigit()):
            raise TypeError("Both inputs must be numbers.")
        
        # Convert to floats
        num1 = float(num1)
        num2 = float(num2)
        
        print(f"Numbers entered successfully: {num1}, {num2}")
    except TypeError as e:
        print(f"TypeError: {e}")

if __name__ == "__main__":
    get_numbers()
