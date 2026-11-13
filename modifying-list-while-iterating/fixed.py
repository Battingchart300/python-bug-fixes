"""FIXED: iterate over a copy, or build a new list.

The bug: deleting from a list while iterating over it shifts the
remaining items left, so the loop skips the element that slid into
the removed slot. The fix: loop over a copy (numbers[:]) and delete
from the original — or, cleaner, build a new list with a comprehension.
"""

numbers = [2, 4, 6, 8]
for n in numbers[:]:  # iterate over a copy
    if n % 2 == 0:
        numbers.remove(n)

print(numbers)  # []

# The cleaner way: keep only what you want
numbers = [2, 4, 6, 8]
numbers = [n for n in numbers if n % 2 != 0]
print(numbers)  # []
