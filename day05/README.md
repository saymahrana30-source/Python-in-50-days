# Day 05 — Strings Deep Dive

_Week 1: Fundamentals (Days 1-10)_

## Topics Covered
- String indexing & slicing
- String methods (.split, .join, .strip, .replace, .format)
- Immutability
- Palindrome/anagram patterns

## Notes
- Strings are immutable - every 'modification' method returns a new string.
- Slicing syntax s[start:stop:step] also works in reverse with s[::-1].
- '.join()' is the preferred way to concatenate many strings (faster than repeated +).

## Today's Challenge
Write a function that checks if two strings are anagrams of each other, and another that reverses words in a sentence.

## Interview Questions
**Q: Why is string immutability important in Python?**

A: It makes strings hashable (usable as dict keys) and safe to share across references without unexpected side effects.

**Q: What's the fastest way to concatenate a list of strings?**

A: ''.join(list_of_strings) - it's O(n), whereas repeated += in a loop is O(n^2) due to new string creation each time.

## Files
- `exercises.py` — space to attempt today's challenge yourself first
- `solutions.py` — a reference approach (write your own before peeking)
