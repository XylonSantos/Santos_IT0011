vowels = "aeiouAEIOU"
consonants = 0
vowels_count = 0
spaces = 0
others = 0

input_string = input("Enter a string: ")

for char in input_string:
    if char.isalpha():
        if char in vowels:
            vowels_count += 1
        else:
            consonants += 1
    elif char.isspace():
        spaces += 1
    else:
        others += 1

print(f"Vowels: {vowels_count}")
print(f"Consonants: {consonants}")
print(f"Spaces: {spaces}")
print(f"Other characters: {others}")