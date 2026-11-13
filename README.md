# Python Bug Fixes

Common Python bugs fixed and explained — real broken scripts with before and after code and what went wrong.

Each bug has its own folder with two files:

| File | What it is |
| --- | --- |
| `broken.py` | The buggy version — run it and see the bug happen |
| `fixed.py` | The fixed version — run it and see the correct result |

## Bugs

| Folder | Bug | In short |
| --- | --- | --- |
| `mutable-default-arg/` | Mutable default argument | `def f(x=[])` shares one list between all calls |
| `late-binding-closures/` | Late binding closures | A `lambda` in a loop sees the last loop value, not the one from its own round |
| `modifying-list-while-iterating/` | Modifying a list while iterating | Deleting from a list while looping over it skips elements |

## How to use it

```bash
# See the bug happen
python mutable-default-arg/broken.py

# See the fix work
python mutable-default-arg/fixed.py
```

## License

MIT — see `LICENSE`.
