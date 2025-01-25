"""
Sorting an Array of Integers. First, populate an array programmatically with 10,000
integers. Use Random number generation. Integers should be positive and negative and be
between -50 to +50. Print the frequency distribution. Next use any algorithm from the
following: Quick sort, Merge Sort to sort the array. Print out your result.
"""

import random
from collections import Counter

# Step 1: Generate an array of 10,000 random integers between -50 and 50
gen_array = [random.randint(-50, 50) for _ in range(10000)]

# Step 2: Print the frequency distribution in a formatted table
print("Frequency Distribution (Number: Count):")
frequency = Counter(gen_array)
for number, count in sorted(frequency.items()):
    print(f"{number:3}: {count:5}")

# Step 3: Merge Sort Implementation
def merge_sort(arr):
    # Base case: array with 1 or fewer elements is already sorted
    if len(arr) <= 1:
        return arr

    # Find the middle of the array
    mid_of_array = len(arr) // 2

    # Divide the array into two halves
    left_half_of_array = arr[:mid_of_array]
    right_half_of_array = arr[mid_of_array:]

    # Recursively sort each half
    left_half_of_array = merge_sort(left_half_of_array)
    right_half_of_array = merge_sort(right_half_of_array)

    # Merge the sorted halves
    return merge(left_half_of_array, right_half_of_array)

def merge(left, right):
    merged = []
    i = j = 0
    # Merge the two arrays in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    # Append remaining elements from either left or right array
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# Step 4: Sort the array using Merge Sort
sorted_array = merge_sort(gen_array)

# Step 5: Print the sorted array in a more readable format
print("\nSorted Array (first 20 elements):")
print(sorted_array[:20])  # Display only the first 20 elements for readability
