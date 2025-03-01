first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")

full_name = first_name + " " + last_name

sliced_name = first_name[:3]

greeting_message = "Hello, " + sliced_name + "! Welcome. You are " + age + " years old."

print()
print("Full Name: " + full_name)
print("Sliced Name: " + sliced_name)
print(greeting_message)