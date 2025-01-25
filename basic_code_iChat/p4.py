"""Write a Python program that prompts the user to enter 10 numbers.
The program should then filter and display the even and odd numbers separately.
Ensure your program handles the input of any valid numerical values."""

def filter_even_odd():
    print("Welcome to the Even and Odd Number Filter!")

    try:
        # Prompt the user to enter 10 numbers in a single input separated by spaces
        user_input = input("Please enter 10 numbers separated by spaces: ").strip()
        
        # Convert the input into a list of numbers
        numbers = list(map(float, user_input.split()))
        
        # Check if exactly 10 numbers are entered
        if len(numbers) != 10:
            raise ValueError("You must enter exactly 10 numbers.")

        # Separate even and odd numbers
        even_numbers = [num for num in numbers if num % 2 == 0]
        odd_numbers = [num for num in numbers if num % 2 != 0]

        # Display the results
        print("\nEven numbers:")
        print(even_numbers if even_numbers else "None")

        print("\nOdd numbers:")
        print(odd_numbers if odd_numbers else "None")

    except ValueError as e:
        # Handle invalid input
        print(f"\nInvalid input: {e}")

if __name__ == "__main__":
    filter_even_odd()
