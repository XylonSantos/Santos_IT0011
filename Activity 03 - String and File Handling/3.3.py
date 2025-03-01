last_name = input("Enter last name: ")
first_name = input("Enter first name: ")
age = input("Enter age: ")
contact_number = input("Enter contact number: ")
course = input("Enter course: ")

student_info = "Last Name: " + last_name + "\n" + \
               "First Name: " + first_name + "\n" + \
               "Age: " + age + "\n" + \
               "Contact Number: " + contact_number + "\n" + \
               "Course: " + course + "\n"

with open("students.txt", "a") as file:
    file.write(student_info)

print("\nStudent information has been saved to 'students.txt'.")