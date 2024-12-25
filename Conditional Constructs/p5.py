#Q5  Atransport company charges the fare according to following table:
# User input
distance = int(input("Enter the distance: "))
#conditions for checking the criteria
if 1 <= distance <= 50:
    print("Your charges are 8 Rs./km")
    total_charge = distance * 8
    print(f"Distance is {distance} km and charges will be {total_charge} Rs.")
elif 51 <= distance <= 100:
    print("Your charges are 10 Rs./km")
    total_charge = distance * 10
    print(f"Distance is {distance} km and charges will be {total_charge} Rs.")
elif distance > 100:
    print("Your charges are 12 Rs./km")
    total_charge = distance * 12
    print(f"Distance is {distance} km and charges will be {total_charge} Rs.")
else:
    print("Invalid distance entered. Please enter a positive distance.")
        
