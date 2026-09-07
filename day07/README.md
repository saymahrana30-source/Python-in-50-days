# Day 07 — Tuples & Sets

_Week 1: Fundamentals (Days 1-10)_

## Topics Covered
- Tuple immutability & use cases
- Tuple unpacking
- Set operations (union, intersection, difference)
- When to use set vs list

## Notes
- Tuples are immutable - use them for fixed collections like coordinates or function returns.
- Sets automatically remove duplicates and give O(1) average membership checks (in).
- Set operations (|, &, -, ^) map directly to union, intersection, difference, symmetric difference.

## Today's Challenge
Given two lists of student names in different classes, use sets to find students in both, only in class A, and only in class B.

## Interview Questions
**Q: Why would you choose a set over a list?**

A: When you need fast membership testing or automatic de-duplication - set lookups are O(1) average vs O(n) for lists.

**Q: Why are tuples hashable but lists aren't?**

A: Tuples are immutable so their contents can't change after hashing, making them safe as dict keys or set members; lists can mutate, breaking that guarantee.

## Files
- `exercises.py` — space to attempt today's challenge yourself first
- `solutions.py` — a reference approach (write your own before peeking)
