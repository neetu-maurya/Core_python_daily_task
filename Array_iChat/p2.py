#Take a 2-dimensional array as a user input. Print it out. Swap the rows as columns.
#Print it out.
# Step 1: Get a 2D array as input from the user
try:
    print("Enter a 2D array row by row, with numbers separated by spaces.")
    print("Example:")
    print("Input:")
    print("1 2 3")
    print("4 5 6")
    print("Type 'done' to finish input.\n")
    
    # Initialize an empty list to store rows
    array_2d = []

    # Read rows from the user until 'done' is entered
    while True:
        row_input = input("Enter row (or type 'done' to finish): ")
        if row_input.lower() == 'done':
            break
        # Convert the space-separated row into a list of integers
        row = list(map(int, row_input.split()))
        array_2d.append(row)

    # Print the original 2D array
    print("\nOriginal 2D Array:")
    for row in array_2d:
        print(row)

    # Step 2: Transpose the 2D array (swap rows and columns)
    # Use the zip function to transpose
    transposed_array = [list(column) for column in zip(*array_2d)]

    # Print the transposed 2D array
    print("\nTransposed 2D Array (Rows as Columns):")
    for row in transposed_array:
        print(row)

except ValueError:
    print("Invalid input! Please enter numbers separated by spaces.")
