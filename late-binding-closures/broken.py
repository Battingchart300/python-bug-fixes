"""BROKEN: lambdas created in a loop share the loop variable.

The lambda does NOT capture the value of i from its own round of the
loop — it looks up i when it is CALLED. By then the loop is finished
and i is 2 (the last value), so every function returns 2.

Run it: all three should print 0, 1, 2 — but all print 2.
"""

functions = []
for i in range(3):
    functions.append(lambda: i)

for f in functions:
    print(f())  # expected: 0, 1, 2 — actual: 2, 2, 2
