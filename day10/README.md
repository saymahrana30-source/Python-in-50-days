# Day 10 — Functions Advanced + Week 1 Review

_Week 1: Fundamentals (Days 1-10)_

## Topics Covered
- *args & **kwargs
- Lambda functions
- map/filter/reduce
- Week 1 mini project

## Notes
- *args collects extra positional arguments into a tuple; **kwargs collects extra keyword args into a dict.
- Lambdas are anonymous one-line functions, best used for short throwaway logic (e.g. sort keys).
- map/filter return iterators in Python 3 - wrap in list() to see results directly.

## Today's Challenge
MINI PROJECT: Build a command-line calculator that supports +,-,*,/,** and history tracking, using functions with *args.

## Interview Questions
**Q: When would you use a lambda instead of a regular function?**

A: For short, throwaway logic passed inline - e.g. as a key= argument to sorted() or filter(). Anything more than one line should be a named function.

**Q: What do *args and **kwargs let you do?**

A: They let a function accept a variable number of positional (*args) or keyword (**kwargs) arguments without defining them all explicitly.

## Files
- `exercises.py` — space to attempt today's challenge yourself first
- `solutions.py` — a reference approach (write your own before peeking)
