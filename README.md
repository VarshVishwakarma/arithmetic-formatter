# arithmetic-formatter
A Python program that formats arithmetic problems vertically with proper spacing and optional solutions. Built as part of freeCodeCamp’s Scientific Computing with Python.

# Arithmetic Formatter (Python)

A Python program that takes multiple arithmetic problems as input (addition and subtraction) and arranges them vertically, just like they appear on paper. Includes validation and an optional feature to display solutions.

---

## Features
- Supports up to 5 problems at a time
- Handles addition and subtraction
- Input validation:
  - Operator must be `+` or `-`
  - Numbers must contain digits only
  - Numbers cannot exceed 4 digits
- Option to display solutions

---

## Example

```python
from main import arithmetic_arranger

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
