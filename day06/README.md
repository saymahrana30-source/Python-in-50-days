# Day 06 — Lists

_Week 1: Fundamentals (Days 1-10)_

## Topics Covered
- List creation & indexing
- append/insert/remove/pop
- Slicing
- Sorting (sort vs sorted)
- Nested lists

## Notes
- Lists are mutable and ordered - they're the default 'array' type in Python.
- list.sort() modifies in place and returns None; sorted(list) returns a new sorted list.
- Slicing a list always returns a new list, even if the slice is the whole thing.

## Today's Challenge
Write a program that manages a to-do list in a Python list: add, remove, mark complete, and print status - all via a menu loop.

## Interview Questions
**Q: What's the difference between .sort() and sorted()?**

A: .sort() mutates the original list and returns None. sorted() returns a new sorted list, leaving the original untouched.

**Q: How do you remove duplicates from a list while preserving order?**

A: Use dict.fromkeys(list) (Python 3.7+ dicts preserve insertion order) or a loop with a seen-set check.

## Files
- `exercises.py` — space to attempt today's challenge yourself first
- `solutions.py` — a reference approach (write your own before peeking)
