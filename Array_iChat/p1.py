"""Populate a number array through user input. Example: 2,3,4,5,14,10,4. Identify the index where the sum of left digits equals the sum of right digits. Call it a "Balance Index". The code should print out the Balance Index. If no Balance Index exists - it should say so.
In the example array, the Balance Index is 4 """
def find_balance_index(arr):
    for i in range(len(arr)):
        left_sum = sum(arr[:i])  # Sum of elements to the left of index i
        right_sum = sum(arr[i+1:])  # Sum of elements to the right of index i
        if left_sum == right_sum:
            return i
    return -1  # Return -1 if no Balance Index exists

# Input from the user
try:
    user_input = input("Enter numbers separated by commas (e.g., 2,3,4,5,14,10,4): ")
    array = list(map(int, user_input.split(',')))
    balance_index = find_balance_index(array)
    if balance_index != -1:
        print(f"The Balance Index is: {balance_index}")
    else:
        print("No Balance Index exists in the array.")
except ValueError:
    print("Invalid input. Please enter a valid list of integers separated by commas.")
