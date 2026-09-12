# Day 13 — Inheritance

_Week 2: OOP & Intermediate (Days 11-20)_

## Topics Covered
- Parent/child classes
- super()
- Method overriding
- Multiple inheritance basics

## Notes
- Inheritance lets a child class reuse and extend a parent class's behavior.
- super().__init__() calls the parent's constructor - essential when overriding __init__ in a subclass.
- Method overriding means redefining a parent method in the child with the same name.

## Today's Challenge
Create an Animal base class and Dog/Cat subclasses that override a speak() method differently for each.

## Interview Questions
**Q: What does super() do and when do you need it?**

A: It gives access to the parent class's methods, most commonly to call the parent's __init__ so the subclass doesn't have to duplicate its setup logic.

**Q: What is method overriding?**

A: When a subclass defines a method with the same name as one in its parent class, replacing the parent's behavior for that subclass.

## Files
- `exercises.py` — space to attempt today's challenge yourself first
- `solutions.py` — a reference approach (write your own before peeking)
