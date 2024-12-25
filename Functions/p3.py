3. Using max() and min() functions display the maximum and minimum of 5 random
numbers.

# Function to take input and find max and min
def find_max_min():
    # Taking 5 random numbers as input from the user
    numbers = [int(input(f"Enter number {i+1}: ")) for i in range(5)]
    
    # Using max() and min() to find the maximum and minimum values
    maximum = max(numbers)
    minimum = min(numbers)
    
    # Display the results
    print("The maximum number is:", maximum)
    print("The minimum number is:", minimum)

# Calling the function
find_max_min()
