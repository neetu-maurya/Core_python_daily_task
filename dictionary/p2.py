'''2.Write a Python script to concatenate the following dictionaries to create a new one.

Sample Dictionary :

dic1={1:10, 2:20}

dic2={3:30, 4:40}

dic3={5:50,6:60}

Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}'''



# Function to take user input for a dictionary
def get_user_input():
    user_dict = {}
    print("Enter key-value pairs for the dictionary. Type 'stop' to finish.")
    while True:
        key = input("Enter key (or 'stop' to end): ")
        if key.lower() == 'stop':
            break
        value = input("Enter value: ")
        user_dict[key] = value
    return user_dict

# Taking dictionaries as input from the user
dic1 = get_user_input()
dic2 = get_user_input()
dic3 = get_user_input()

# Concatenating dictionaries
result = {**dic1, **dic2, **dic3}

# Print the result
print("Concatenated Dictionary:", result)
