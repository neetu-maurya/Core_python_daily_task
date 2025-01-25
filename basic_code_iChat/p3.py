"""Write a Python program that takes two numbers as input from the user,
swaps their values, and then prints the swapped values.
Ensure your program handles the input of any valid numerical values."""
def swap_numbers():
    print("Welcome to the Number Swapper!")

    try:
        # Prompt the user for the first number
        num1 = float(input("Enter the first number: ").strip())

        # Prompt the user for the second number
        num2 = float(input("Enter the second number: ").strip())

        # Swap the numbers
        num1, num2 = num2, num1

        # Display the swapped values
        print("\nAfter swapping:")
        print(f"First number: {num1}")
        print(f"Second number: {num2}")

    except ValueError:
        # Handle invalid input
        print("\nInvalid input! Please enter valid numerical values.")

if __name__ == "__main__":
    swap_numbers()
