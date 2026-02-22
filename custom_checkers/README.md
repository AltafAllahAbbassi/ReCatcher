# Custom Pylint Rules for ReCatcher

This directory contains custom Pylint checkers implemented for detecting inefficiencies not natively supported by Pylint.

## Implemented Checkers

### 1. UnnecessaryConditionalBlockChecker

Detects `if` statements where both branches return constant boolean values:

```python
if condition:
    return True
else:
    return False
```

These constructs can be simplified to:

``` return condition ```

The checker analyzes the AST and verifies:

- Both ```if``` and ```else``` blocks contain exactly one statement

- Both statements are ```return```

- The return values are constant booleans (```True``` and ```False```)
