""" 3. Write a Python program to calculate the sum of the numbers in a given tuple.
 Input: tuples_list = [(1, 2), (3, 4), (5, 6)]"""

# Input: Tuples from the user
user_input = input("Enter the list of tuples (e.g., (1,2),(3,4),(5,6)): ")

# Convert the input string to a list of tuples
tuples_list = eval(user_input)  # Note: Use with caution for trusted input only

# Calculate the sum of all numbers in the list of tuples
total_sum = sum(sum(t) for t in tuples_list)

# Output the result
print("Sum of all numbers in the tuple list:", total_sum)
