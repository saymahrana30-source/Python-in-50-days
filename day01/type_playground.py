"""
Day 1 — Type Playground
A scratch file for experimenting with Python's data types and conversions.
Run this and read the output to build intuition, don't just skim it.
"""

# --- type() checks ---
x = 5
y = 5.0
z = "5"
w = True

print(type(x), type(y), type(z), type(w))

# --- safe vs unsafe conversions ---
print(int("42"))          # works fine
print(float("3.14"))      # works fine
print(int(float("3.14")))  # works — convert to float first, then truncate to int

try:
    print(int("3.14"))    # fails — int() can't parse a decimal string directly
except ValueError as e:
    print(f"int('3.14') failed as expected: {e}")

try:
    print(int("abc"))     # fails — not a number at all
except ValueError as e:
    print(f"int('abc') failed as expected: {e}")

# --- bool quirks worth remembering ---
print(bool(0), bool(1), bool(""), bool("false"))
# bool("false") is True! Any non-empty string is truthy, regardless of content.

# --- string <-> number concatenation ---
age = 20
# print("Age: " + age)  # this would raise a TypeError — can't concat str + int
print("Age: " + str(age))  # must convert explicitly
