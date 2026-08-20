character = input("Enter one character: ")

if len(character) != 1:
    print("Please enter exactly one character.")
else:
    ascii_value = ord(character)
    binary_value = format(ascii_value, "08b")

    print("Character:", character)
    print("ASCII/Unicode value:", ascii_value)
    print("Binary value:", binary_value)
