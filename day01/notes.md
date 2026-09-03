# Day 1 — Variables, Data Types, Basic I/O

## Topics covered
- Variables and assignment (no type declaration needed)
- Core data types: `int`, `float`, `str`, `bool`
- Type checking with `type()`
- Type conversion: `int()`, `str()`, `float()`
- `input()` for reading user input (always returns a string!)
- `print()` — formatting output, f-strings

## Key points
- Python is dynamically typed: `x = 5` then `x = "hello"` is legal (the variable just points to a new object).
- `input()` ALWAYS returns a string — convert it manually if you need a number: `age = int(input("Age: "))`.
- f-strings (`f"Hello {name}"`) are the modern, preferred way to format output — cleaner than `.format()` or `%`.

## Practice
Wrote `main.py` — a small "profile card generator" that takes name, age, and city from the user and prints a formatted summary. Also wrote `type_playground.py` to experiment with type conversions and see what breaks (e.g. `int("abc")` raises `ValueError`).

## Questions / things to revisit
- Why does `int("3.5")` fail but `float("3.5")` works? → `int()` can't parse decimal points directly, need `int(float("3.5"))` if truncation is intended.
