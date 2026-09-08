# Day 08 — Dictionaries

_Week 1: Fundamentals (Days 1-10)_

## Topics Covered
- Key-value pairs
- get/keys/values/items
- Nested dictionaries
- Dictionary comprehensions intro

## Notes
- dict.get(key, default) avoids KeyError - safer than d[key] when the key might not exist.
- Dicts preserve insertion order since Python 3.7, which is often relied on in real code.
- Nested dicts are how you represent JSON-like structures natively in Python.

## Today's Challenge
Build a simple contact book using a dictionary of dictionaries (name -> {phone, email}), with add/search/delete via a menu.

## Interview Questions
**Q: What happens if you access a missing key with d[key] vs d.get(key)?**

A: d[key] raises a KeyError; d.get(key) returns None (or a specified default) without raising.

**Q: How would you merge two dictionaries in Python?**

A: Using {**dict1, **dict2} or dict1 | dict2 (Python 3.9+) - later keys overwrite earlier ones on conflict.

## Files
- `exercises.py` — space to attempt today's challenge yourself first
- `solutions.py` — a reference approach (write your own before peeking)
