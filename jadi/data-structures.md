# Data Structures

## Precedence

| Effective Precedence | Operator(s)         | Description                    | Associativity |
| -------------------- | ------------------- | ------------------------------ | ------------- |
| Highest              | `()`                | **Grouping (parentheses)**     | N/A           |
| 1                    | `**`                | Exponentiation                 | Right-to-left |
| 2                    | `+x`, `-x`, `~x`    | Unary plus, minus, bitwise NOT | Right-to-left |
| 3                    | `*`, `/`, `//`, `%` | Multiplication, division, etc. | Left-to-right |
| 4                    | `+`, `-`            | Addition, subtraction          | Left-to-right |

## Operators

- in python 3.0, `/` always returns a float.
- `//` returns the integer result.
- `%` is the mod operator, `10%3 = 1`


