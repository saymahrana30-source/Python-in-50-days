# Day 03 — Control Flow: if / elif / else

_Week 1: Fundamentals (Days 1-10)_

## Topics Covered
- Conditional statements
- Nested conditionals
- Comparison chaining
- Truthy vs falsy values

## Notes
- Python allows chained comparisons like 0 < x < 10, which is cleaner than most languages.
- Falsy values: 0, 0.0, '', [], {}, None, False. Everything else is truthy.
- Avoid deeply nested if/else - prefer early returns or elif chains for readability.

## Today's Challenge
Write a grading script: takes a score (0-100) as input and prints the letter grade (A/B/C/D/F).

## Interview Questions
**Q: What values are considered 'falsy' in Python?**

A: 0, 0.0, empty string, empty list/dict/tuple/set, None, and False. Everything else is truthy.

**Q: What's the difference between elif and multiple separate if statements?**

A: elif stops checking once one condition matches; separate ifs each evaluate independently, which can run multiple blocks unintentionally.

## Files
- `exercises.py` — space to attempt today's challenge yourself first
- `solutions.py` — a reference approach (write your own before peeking)
