binary_one = input("Enter the first binary number: ")
binary_two = input("Enter the second binary number: ")

valid_digits = {"0", "1"}

if (
    not binary_one
    or not binary_two
    or not set(binary_one).issubset(valid_digits)
    or not set(binary_two).issubset(valid_digits)
):
    print("Invalid input! A binary number can contain only 0 and 1.")
else:
    decimal_one = int(binary_one, 2)
    decimal_two = int(binary_two, 2)

    decimal_sum = decimal_one + decimal_two
    binary_sum = bin(decimal_sum)[2:]

    print("First decimal value:", decimal_one)
    print("Second decimal value:", decimal_two)
    print("Decimal sum:", decimal_sum)
    print("Binary sum:", binary_sum)
