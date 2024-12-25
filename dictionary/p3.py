'''3.Write a Python program to get the key, value and item in a dictionary.

Accept the input as a employee details. name,no, ID, dep , des,DOJ, DOB, salary'''

# Program to get key, value, and item from a dictionary of employee details

# Function to take employee details as input
def get_employee_details():
    employee_dict = {}
    print("Enter employee details:")
    employee_dict["name"] = input("Enter Name: ")
    employee_dict["no"] = input("Enter Number: ")
    employee_dict["ID"] = input("Enter ID: ")
    employee_dict["dep"] = input("Enter Department: ")
    employee_dict["des"] = input("Enter Designation: ")
    employee_dict["DOJ"] = input("Enter Date of Joining (DOJ): ")
    employee_dict["DOB"] = input("Enter Date of Birth (DOB): ")
    employee_dict["salary"] = input("Enter Salary: ")
    return employee_dict

# Get employee details from the user
employee_details = get_employee_details()

# Display keys, values, and items in the dictionary
print("\nEmployee Details:")
print("Keys:", employee_details.keys())
print("Values:", employee_details.values())
print("Items:", employee_details.items())
