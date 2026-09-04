# Day 02 — Operators & Type Conversion

_Week 1: Fundamentals (Days 1-10)_

## Topics Covered
- Arithmetic operators (+ - * / // % **)
- Comparison & logical operators
- Implicit vs explicit conversion
- Operator precedence

## Notes
- // is floor division, % is modulus (remainder) - both are used constantly in problem solving.
- Comparison operators return bool; logical operators (and/or/not) combine bools.
- Implicit conversion happens automatically (int + float = float); explicit needs int()/str()/float().

## Today's Challenge
Build a simple unit converter (e.g. km to miles) that handles user input safely with type conversion.

## Interview Questions
**Q: What's the difference between / and // in Python?**

A: / always returns a float (true division). // returns the floored (rounded down) integer result.

**Q: What is operator precedence and why does it matter?**

A: It determines the order operations run in (e.g. * before +). Misunderstanding it causes silent logic bugs.

## Files
- `exercises.py` — space to attempt today's challenge yourself first
- `solutions.py` — a reference approach (write your own before peeking)
