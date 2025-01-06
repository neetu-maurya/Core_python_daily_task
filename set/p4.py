"""4. Write a Python program to Remove items from set1 that are not common to
 both set1 and set2.
Input:
 set1 = {10, 20, 30, 40, 50}
 set2 = {30, 40, 50, 60, 70}
 Output:
 {40, 50, 30}"""

# Input: Two sets from the user
set1 = set(map(int, input("Enter the elements of the first set, separated by commas: ").split(',')))
set2 = set(map(int, input("Enter the elements of the second set, separated by commas: ").split(',')))

# Retain only items common to both sets
set1.intersection_update(set2)

# Output the result
print("Output:", set1)
