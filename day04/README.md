# Day 04 — Loops: for & while

_Week 1: Fundamentals (Days 1-10)_

## Topics Covered
- for loops over ranges/sequences
- while loops
- break, continue, else on loops
- range() function

## Notes
- range(start, stop, step) is exclusive of stop - a common off-by-one bug source.
- break exits a loop entirely; continue skips to the next iteration.
- Python loops can have an else clause that runs only if the loop completes without break.

## Today's Challenge
Write a number-guessing game: the program picks a random number 1-100, user guesses in a while loop with hints ('higher'/'lower').

## Interview Questions
**Q: When would you use a while loop instead of a for loop?**

A: When the number of iterations isn't known in advance and depends on a condition (e.g. waiting for valid input).

**Q: What does the else clause on a for loop do?**

A: It runs only if the loop finishes without hitting a break - useful for 'search and not found' patterns.

## Files
- `exercises.py` — space to attempt today's challenge yourself first
- `solutions.py` — a reference approach (write your own before peeking)
