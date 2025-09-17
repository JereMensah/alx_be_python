#!/usr/bin/env python3
"""
Pattern Drawing Program
This script prompts the user for a positive integer and prints a square pattern
of that size using nested loops (while + for).
"""

# Prompt the user for input
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer loop (while) to go through each row
while row < size:
    # Inner loop (for) to print asterisks in the current row
    for col in range(size):
        print("*", end="")
    # Move to next line after finishing a row
    print()
    row += 1
