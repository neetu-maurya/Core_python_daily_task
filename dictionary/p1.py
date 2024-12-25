
'''1. Write a Python program and calculate the mean of the below dictionary.

Accept student anme as key and in value accept marks'''

# Program to calculate the mean of marks

def calculate_mean(marks_dict):
    # Check if the dictionary is empty
    if not marks_dict:
        print("The dictionary is empty. No mean to calculate.")
        return None

    # Calculate the mean
    total_marks = sum(marks_dict.values())
    number_of_students = len(marks_dict)
    mean = total_marks / number_of_students

    return mean

# Accepting input from the user
marks_dict = {}
print("Enter student names and their marks. Type 'stop' to finish.")
while True:
    student_name = input("Enter student name (or 'stop' to end): ")
    if student_name.lower() == 'stop':
        break

    try:
        marks = float(input(f"Enter marks for {student_name}: "))
        marks_dict[student_name] = marks
    except ValueError:
        print("Please enter a valid number for marks.")

# Display the mean if the dictionary is not empty
if marks_dict:
    mean = calculate_mean(marks_dict)
    print(f"The mean of the marks is: {mean:.2f}")
else:
    print("No data to calculate the mean.")
