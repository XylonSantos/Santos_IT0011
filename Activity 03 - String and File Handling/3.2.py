first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

full_name = first_name + " " + last_name

full_name_upper = full_name.upper()
full_name_lower = full_name.lower()

length_of_full_name = len(full_name)

print()
print("Full Name: " + full_name)
print("Full Name (Upper Case): " + full_name_upper)
print("Full Name (Lower Case): " + full_name_lower)
print("Length of Full Name: " + str(length_of_full_name))