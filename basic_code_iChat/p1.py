"""Write a Python program that accepts an array of numbers from the user and display
the numbers in ascending order. Ensure your program handles any valid number
of elements in the array."""

def main():
    # Prompt the user to enter numbers separated by spaces
    print("Please enter a series of numbers separated by spaces:")
    input_numbers = input().strip()

    try:
        # Convert the input string into a list of floating-point numbers
        number_list = list(map(float, input_numbers.split()))
        
        # Sort the numbers in ascending order
        sorted_numbers = sorted(number_list)

        # Display the sorted numbers
        print("\nThe numbers in ascending order are:")
        print(" ".join(map(str, sorted_numbers)))

    except ValueError:
        # Handle cases where the input is not valid (e.g., contains non-numeric values)
        print("\nInvalid input! Make sure to enter only numbers separated by spaces.")

# Execute the main function when the script is run
if __name__ == "__main__":
    main()

