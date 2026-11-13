"""FIXED: bind the current value with a default argument.

The bug: a lambda (or any closure) created in a loop looks up the loop
variable when it is called, not when it is created — so every function
sees the last value. The fix: capture the value now with a default
argument (i=i), which is evaluated when the lambda is defined.
"""

functions = []
for i in range(3):
    functions.append(lambda i=i: i)

for f in functions:
    print(f())  # 0, 1, 2
