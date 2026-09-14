# Day 15 — Magic / Dunder Methods

_Week 2: OOP & Intermediate (Days 11-20)_

## Topics Covered
- __str__ vs __repr__
- __len__, __eq__, __add__
- Operator overloading

## Notes
- __str__ defines the user-friendly print() output; __repr__ is the developer-facing, unambiguous representation.
- Overloading __eq__ lets you define what == means for your custom objects.
- Dunder methods are how Python lets built-in functions like len(), str(), and operators work on custom classes.

## Today's Challenge
Give your Book class __str__, __eq__ (compare by title+author), and __lt__ (compare by page count) so a list of Books can be sorted.

## Interview Questions
**Q: What's the difference between __str__ and __repr__?**

A: __str__ is meant to be readable/user-facing (used by print() and str()); __repr__ should be unambiguous, ideally something that could recreate the object, and is used by the interpreter/debugger.

**Q: How does Python know how to sort a list of custom objects?**

A: It uses comparison dunder methods like __lt__ that you define on the class; sorted() and list.sort() call these under the hood.

## Files
- `exercises.py` — space to attempt today's challenge yourself first
- `solutions.py` — a reference approach (write your own before peeking)
