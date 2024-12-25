
""" 4. Atoy vendor supplies three types of toys: Battery Based Toys, Key-based
 Toys, and Electrical Charging Based Toys. The vendor gives a discount of
 10% on orders for battery-based toys if the order is for more than Rs. 1000.
 On orders of more than Rs. 100 for key-based toys, a discount of 5% is
 given, and a discount of 10% is given on orders for electrical charging based
 toys of value more than Rs. 500. Assume that the numeric codes 1,2 and 3
 are used for battery based toys, key-based toys, and electrical charging based
 toys respectively. Write a program that reads the product code and the order
 amount and prints out the net amount that the customer is required to pay
 after the discount."""

# Define numeric codes for toys
Battery_Based_Toys = 1
Key_Based_Toys = 2
Electrical_Charging_Based_Toys = 3

# Input from the user
print("Battery Based Toy press: 1\nKey Based Toy press: 2\nCharging Based Toy press: 3")
user = int(input("Enter your choice: "))
order = float(input("Enter your order amount: "))

# Discount criteria and calculation
if user == 1:  # Battery Based Toys
    if order > 1000:
        discount = order * (10 / 100)  # 10% discount
        total_amount = order - discount
        print("You get a 10% discount.")
    else:
        total_amount = order
        print("You don't get any discount.")
elif user == 2:  # Key Based Toys
    if order > 100:
        discount = order * (5 / 100)  # 5% discount
        total_amount = order - discount
        print("You get a 5% discount.")
    else:
        total_amount = order
        print("You don't get any discount.")
elif user == 3:  # Electrical Charging Based Toys
    if order > 500:
        discount = order * (10 / 100)  # 10% discount
        total_amount = order - discount
        print("You get a 10% discount.")
    else:
        total_amount = order
        print("You don't get any discount.")
else:
    print("Invalid choice.")
    total_amount = 0  # No calculation for invalid choice

# Final amount
if total_amount > 0:
    print(f"Your final amount is: {total_amount}")
