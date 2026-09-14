# Day 16 — File Handling

_Week 2: OOP & Intermediate (Days 11-20)_

## Topics Covered
- open() modes (r, w, a, r+)
- with statement / context managers
- Reading/writing text files
- Working with CSV basics

## Notes
- Always use 'with open(...) as f' - it auto-closes the file even if an error occurs.
- Mode 'w' overwrites the file entirely; 'a' appends without erasing existing content.
- readlines() loads the whole file into memory as a list - fine for small files, risky for huge ones.

## Today's Challenge
Write a script that logs each to-do list action (from Day 6) to a text file with a timestamp, and can replay the log on startup.

## Interview Questions
**Q: Why use 'with open(...)' instead of open()/close() manually?**

A: The with block guarantees the file is closed automatically, even if an exception is raised inside it - manual close() calls can be skipped on error.

**Q: What's the difference between 'w' and 'a' file modes?**

A: 'w' truncates and overwrites the file from scratch; 'a' appends new content to the end, preserving what's already there.

## Files
- `exercises.py` — space to attempt today's challenge yourself first
- `solutions.py` — a reference approach (write your own before peeking)
