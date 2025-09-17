#!/usr/bin/env python3
"""
Weather Recommendation Program
This script asks the user about the current weather and provides
clothing recommendations using if, elif, and else statements.
"""

# Prompt the user for input
weather = input("What's the weather like today? (sunny/rainy/cold): ").strip().lower()

# Make decision based on input
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
