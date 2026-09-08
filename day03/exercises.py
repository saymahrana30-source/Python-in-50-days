"""
Day 03 — Control Flow: if / elif / else
Challenge: Write a grading script: takes a score (0-100) as input and prints the letter grade (A/B/C/D/F).

Attempt this yourself before checking solutions.py.
"""

# Your code here
print("===== GRADE CALCULATOR ======")

marks = float(input("Enter your marks: "))

if not 0 <= marks <= 100:
    print("Invalid marks! Enter a value between 0 and 100.")

elif marks >= 90:
    print("Your grade is: A")

elif marks >= 80:
    print("Your grade is: B")

elif marks >= 70:
    print("Your grade is: C")

elif marks >= 60:
    print("Your grade is: D")

else:
    print("Your grade is: F")
