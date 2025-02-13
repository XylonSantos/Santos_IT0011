def is_palindrome(n):
    """Check if a number is a palindrome."""
    return str(n) == str(n)[::-1]

with open('C:/Users/Lenovo/Downloads/Santos_IT0011/Technical Midterm Exam/numbers.txt', 'r') as file:
    lines = file.readlines()

for i, line in enumerate(lines, start=1):
    numbers = line.strip().split(',')
    total = sum(int(num) for num in numbers if num.strip().isdigit())

    if is_palindrome(total):
        print(f"Line {i}: {line.strip()} (sum {total}) - Palindrome")
    else:
        print(f"Line {i}: {line.strip()} (sum {total}) - Not a palindrome")