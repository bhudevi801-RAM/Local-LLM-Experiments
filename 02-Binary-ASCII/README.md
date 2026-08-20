# Experiment 02 — Binary and ASCII

## Objective

To understand how computers represent characters using ASCII numbers and binary digits.

## What is ASCII?

ASCII assigns a numeric value to each character.

Examples:

| Character | ASCII value | Binary |
|---|---:|---:|
| A | 65 | 01000001 |
| B | 66 | 01000010 |
| a | 97 | 01100001 |
| 0 | 48 | 00110000 |

## Python Experiment

```python
character = input("Enter one character: ")

ascii_value = ord(character)
binary_value = format(ascii_value, "08b")

print("Character:", character)
print("ASCII value:", ascii_value)
print("Binary value:", binary_value)
```

## Example Output

```text
Enter one character: A
Character: A
ASCII value: 65
Binary value: 01000001
```

## Explanation

- `ord(character)` converts a character into its ASCII/Unicode number.
- `format(value, "08b")` converts the number into an 8-bit binary representation.

## Observation

The character `A` has the numeric value `65`, represented in binary as `01000001`.

## Result

A character was successfully converted into its numeric and binary representations.

## What I Learned

- Computers store characters as numbers
- ASCII maps characters to numeric values
- Binary uses only `0` and `1`
- Python can convert characters into numbers and binary
