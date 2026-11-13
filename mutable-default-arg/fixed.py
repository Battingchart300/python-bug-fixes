"""FIXED: use None as the default and create a fresh list inside.

The bug: a mutable default argument (like []) is created once, when the
function is defined, and shared between all calls. The fix: default to
None, then build a new list on every call.
"""


def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items


print(add_item("apple"))   # ['apple']
print(add_item("banana"))  # ['banana']
print(add_item("cherry"))  # ['cherry']
