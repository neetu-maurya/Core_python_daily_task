# Initialize an empty list to store the input lines
lines = []

print("Enter your words or sentences (press Enter on a blank line to finish):")

# Loop to take input until the user presses Enter without typing anything
while True:
    line = input()  # Take input from the user
    if line == "":  # Check for a blank line to stop
        break
    lines.append(line)  # Add the line to the list

# Combine all lines into a single string, removing newlines
output = " ".join(lines)

# Display the result
print("Processed String:", output)
