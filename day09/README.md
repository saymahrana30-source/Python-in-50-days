# Day 09 — Functions Basics

_Week 1: Fundamentals (Days 1-10)_

## Topics Covered
- def syntax
- Parameters & return values
- Default arguments
- Scope (local vs global)
- Docstrings

## Notes
- Functions should ideally do one thing - this makes them easier to test and reuse.
- Default argument values are evaluated once at function definition time (watch out with mutable defaults!).
- Variables defined inside a function are local unless declared global.

## Today's Challenge
Refactor your Day 1-8 exercises into reusable functions in a single utils.py, each with a docstring.

## Interview Questions
**Q: Why is using a mutable default argument (like a list) dangerous?**

A: The default is created once at def time and shared across all calls, so mutations persist between calls unexpectedly. Use None and create the list inside the function instead.

**Q: What's the difference between a parameter and an argument?**

A: A parameter is the variable name in the function definition; an argument is the actual value passed in when calling it.

## Files
- `exercises.py` — space to attempt today's challenge yourself first
- `solutions.py` — a reference approach (write your own before peeking)
