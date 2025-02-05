input_string = input("Enter a string with digits: ")
total = 0

for char in input_string:
    if char.isdigit():
        total += int(char)

print("Sum of digits:", total)
