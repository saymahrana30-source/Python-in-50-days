# Day 12 — Class vs Instance Variables & Constructors

_Week 2: OOP & Intermediate (Days 11-20)_

## Topics Covered
- Class-level vs instance-level attributes
- Class methods (@classmethod)
- Static methods (@staticmethod)

## Notes
- Class variables are shared across all instances; instance variables are unique per object.
- @classmethod receives the class (cls) instead of the instance - often used for alternate constructors.
- @staticmethod takes neither self nor cls - it's just a regular function namespaced inside the class.

## Today's Challenge
Extend your Book class with a class variable total_books that increments every time a new Book is created, plus a classmethod to report it.

## Interview Questions
**Q: What's the difference between a class variable and an instance variable?**

A: A class variable is shared by every instance of the class; an instance variable is set per-object, usually in __init__.

**Q: When would you use @staticmethod over a regular function outside the class?**

A: When the logic is conceptually related to the class but doesn't need access to self or cls - it's a way to namespace it.

## Files
- `exercises.py` — space to attempt today's challenge yourself first
- `solutions.py` — a reference approach (write your own before peeking)
