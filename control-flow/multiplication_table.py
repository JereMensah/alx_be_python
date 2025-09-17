#!/usr/bin/env python3
"""
Multiplication Table Generator
This script asks the user for a number and prints its multiplication table from 1 to 10.
"""

# Prompt the user for input
number = int(input("Enter a number to see its multiplication table: "))

# Generate and print multiplication table
for i in range(1, 11):  # loop from 1 to 10
    product = number * i
    print(f"{number} * {i} = {product}")

