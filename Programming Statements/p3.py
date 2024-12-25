Q.3) Write a Program to Convert Kilometers to Miles

# Conversion factor: 1 kilometer = 0.621371 miles
km_to_miles_conversion_factor = 0.621371

# Taking input from the user in kilometers
kilometers = float(input("Enter the distance in kilometers: "))

# Converting kilometers to miles
miles = kilometers * km_to_miles_conversion_factor

# Displaying the result
print(f"{kilometers} kilometers is equal to {miles:.2f} miles.")
