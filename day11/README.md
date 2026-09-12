# Day 11 — OOP Basics: Classes & Objects

_Week 2: OOP & Intermediate (Days 11-20)_

## Topics Covered
- class syntax
- __init__ constructor
- self keyword
- Instance attributes vs methods

## Notes
- A class is a blueprint; an object (instance) is a concrete thing built from that blueprint.
- self refers to the specific instance and must be the first parameter of instance methods.
- __init__ runs automatically when you create a new object with ClassName().

## Today's Challenge
Create a Book class (title, author, pages, is_read) with a method to mark it read and display its info.

## Interview Questions
**Q: What is the purpose of the __init__ method?**

A: It's the constructor - it runs automatically when an object is created, to initialize instance attributes.

**Q: Why does every instance method need self as the first parameter?**

A: self is how Python passes a reference to the specific instance the method is being called on, giving access to its attributes.

## Files
- `exercises.py` — space to attempt today's challenge yourself first
- `solutions.py` — a reference approach (write your own before peeking)
