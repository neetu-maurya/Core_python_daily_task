'''1. Write a Python program to count the occurrences of each word in a given sentence string = “To change the overall look of your document.
 To change the look available in the gallery” '''
from collections import Counter

# Given sentence
sentence=input("enter the sentence:")
#sentence = """To change the overall look of your document.
#To change the look available in the gallery"""

# Normalize the text: convert to lowercase and remove punctuation
normalized_sentence = sentence.lower().replace('.', '')

# Split the sentence into words
words = normalized_sentence.split()

# Count occurrences of each word
word_count = Counter(words)

# Display the results
print("Word occurrences:")
for word, count in word_count.items():
    print(f"{word}: {count}")
