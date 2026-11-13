"""BROKEN: a mutable default argument is shared between calls.

The default list [] is created ONCE, when the function is defined —
not fresh on every call. Every call that appends to it changes the
same list, so items from earlier calls "leak" into later ones.

Run it: each call should start with an empty list, but it doesn't.
"""


def add_item(item, items=[]):
    items.append(item)
    return items


print(add_item("apple"))   # expected: ['apple']
print(add_item("banana"))  # expected: ['banana']  — but gets ['apple', 'banana']
print(add_item("cherry"))  # expected: ['cherry']  — but gets all three
