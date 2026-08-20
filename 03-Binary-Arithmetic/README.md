# Experiment 03 — Binary Arithmetic

## Objective

To understand binary addition and perform it using Python.

## Binary Addition Rules

| Operation | Result | Carry |
|---|---:|---:|
| 0 + 0 | 0 | 0 |
| 0 + 1 | 1 | 0 |
| 1 + 0 | 1 | 0 |
| 1 + 1 | 0 | 1 |
| 1 + 1 + 1 | 1 | 1 |

## Manual Example

Add the binary numbers `0101` and `0011`:

```text
   0101
 + 0011
 -------
   1000
```

In decimal:

```text
0101 = 5
0011 = 3
1000 = 8
```

Therefore:

```text
5 + 3 = 8
```

## Python Experiment

```python
binary_one = input("Enter the first binary number: ")
binary_two = input("Enter the second binary number: ")

decimal_one = int(binary_one, 2)
decimal_two = int(binary_two, 2)

decimal_sum = decimal_one + decimal_two
binary_sum = bin(decimal_sum)[2:]

print("Decimal sum:", decimal_sum)
print("Binary sum:", binary_sum)
```

## Example Output

```text
Enter the first binary number: 0101
Enter the second binary number: 0011
Decimal sum: 8
Binary sum: 1000
```

## Explanation

- `int(binary_one, 2)` converts a binary string into a decimal number.
- The two decimal numbers are added using `+`.
- `bin(decimal_sum)` converts the result back into binary.
- `[2:]` removes the `0b` prefix from the binary result.

## Observation

Adding binary `0101` and `0011` produces binary `1000`.

## Result

Two binary numbers were successfully added using Python.

## What I Learned

- The rules of binary addition
- How carrying works in binary
- How to convert binary into decimal
- How to convert a decimal result back into binary
