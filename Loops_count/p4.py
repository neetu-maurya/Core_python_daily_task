#4. Python program to get the Fibonacci series between 0 to 50

# Function to generate Fibonacci series up to a given limit
def fibonacci_series(limit):
    a, b = 0, 1  # Starting values of the Fibonacci sequence
    while a <= limit:
        print(a, end=" ")
        a, b = b, a + b  # Update to the next Fibonacci numbers

# Taking input from the user
limit = int(input("Enter the upper limit for the Fibonacci series: "))

# Generate and display the Fibonacci series
print(f"Fibonacci series up to {limit}:")
fibonacci_series(limit)
