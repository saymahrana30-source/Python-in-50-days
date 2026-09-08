"""
Day 02 — Operators & Type Conversion
Challenge: Build a simple unit converter (e.g. km to miles) that handles user input safely with type conversion.

Attempt this yourself before checking solutions.py.
"""

# Your code here
print("====== KM TO MILES CONVERTER ======")

km = float(input("Enter distance in kilometers: "))

miles = km * 0.621371

print(f"{km} km = {miles:.2f} miles")
