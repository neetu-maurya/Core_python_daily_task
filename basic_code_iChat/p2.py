"""
Write a Python program to calculate Body Mass Index (BMI) based on user
input for weight in kilograms and height in meters. Ensure your program
validates input and provides meaningful feedback to the user. Use the BMI
formula: BMI = weight (kg) / (height (m))^2."""

def calculate_bmi():
    print("Welcome to the BMI Calculator!")

    try:
        # Prompt the user for weight in kilograms
        weight = float(input("Enter your weight in kilograms: ").strip())
        if weight <= 0:
            raise ValueError("Weight must be a positive number.")

        # Prompt the user for height in meters
        height = float(input("Enter your height in meters: ").strip())
        if height <= 0:
            raise ValueError("Height must be a positive number.")

        # Calculate BMI
        bmi = weight / (height ** 2)

        # Provide feedback on BMI
        print("\nYour Body Mass Index (BMI) is: {:.2f}".format(bmi))
        if bmi < 18.5:
            print("You are categorized as underweight.")
        elif 18.5 <= bmi < 24.9:
            print("You are categorized as normal weight.")
        elif 25 <= bmi < 29.9:
            print("You are categorized as overweight.")
        else:
            print("You are categorized as obese.")

    except ValueError as e:
        # Handle invalid input
        print(f"\nInvalid input: {e}")

if __name__ == "__main__":
    calculate_bmi()
