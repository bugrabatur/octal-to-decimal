def octal_to_decimal(octal_str):
    return int(octal_str, 8)

octal_number = input("Enter an octal number: ")
decimal_number = octal_to_decimal(octal_number)
print(f"Decimal equivalent: {decimal_number}")
