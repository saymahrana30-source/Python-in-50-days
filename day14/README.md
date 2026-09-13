# Day 14 — Polymorphism & Encapsulation

_Week 2: OOP & Intermediate (Days 11-20)_

## Topics Covered
- Polymorphism via method overriding
- Public/protected/private (_, __ conventions)
- Property decorators (@property)

## Notes
- Python doesn't enforce true private attributes - _var is a convention (protected), __var triggers name mangling.
- @property lets you expose a method as if it were an attribute, useful for computed values or validation.
- Polymorphism means different classes can be used interchangeably if they share a common interface (e.g. .speak()).

## Today's Challenge
Add a @property to your Book class that computes a 'reading_status' string based on is_read, with validation via a setter.

## Interview Questions
**Q: What's the difference between _var and __var in Python?**

A: _var is a convention signaling 'internal use only' but is still accessible. __var triggers name mangling (renamed to _ClassName__var), making accidental access harder but not impossible.

**Q: What problem does @property solve?**

A: It lets you add validation or computed logic to attribute access/assignment while keeping the clean syntax of a regular attribute (obj.value instead of obj.get_value()).

## Files
- `exercises.py` — space to attempt today's challenge yourself first
- `solutions.py` — a reference approach (write your own before peeking)
