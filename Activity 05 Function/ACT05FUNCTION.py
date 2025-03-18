def divide(num1, num2):
    if num2 == 0:
        return None
    return num1 / num2

def exponentiate(base, exponent):
    return base ** exponent

def remainder(num1, num2):
    if num2 == 0:
        return None
    return num1 % num2

def summation(start, end):
    if end <= start:
        return None
    return sum(range(start, end + 1))

while True:
    print("\nChoose an operation:")
    print("[D] - Divide")
    print("[E] - Exponentiation")
    print("[R] - Remainder")
    print("[F] - Summation")
    print("[Q] - Quit")

    choice = input("Enter your choice: ").strip().upper()

    if choice == 'Q':
        print("Exiting the program.")
        break

    if choice in ['D', 'R']:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if choice == 'D':
            result = divide(num1, num2)
        else:
            result = remainder(num1, num2)

    elif choice == 'E':
        base = float(input("Enter the base: "))
        exponent = float(input("Enter the exponent: "))
        result = exponentiate(base, exponent)

    elif choice == 'F':
        start = int(input("Enter the first number (limit): "))
        end = int(input("Enter the second number (limit): "))
        result = summation(start, end)

    else:
        print("Invalid choice, please try again.")
        continue

    if result is None:
        print("Invalid input provided.")
    else:
        print(f"The result is: {result}")