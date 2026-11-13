"""BROKEN: deleting from a list while iterating over it skips items.

When you remove an item, the list shifts left, but the loop still
moves to the next index — so the element that slid into the removed
slot is never checked.

Run it: every number is even, so the result should be an empty list —
but 4 and 8 survive, because they were skipped.
"""

numbers = [2, 4, 6, 8]
for n in numbers:
    if n % 2 == 0:
        numbers.remove(n)

print(numbers)  # expected: [] — actual: [4, 8]
