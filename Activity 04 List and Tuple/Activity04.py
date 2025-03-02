import json
import os

class StudentRecord:
    def __init__(self, student_id, full_name, class_standing, exam_grade):
        self.student_id = student_id
        self.full_name = full_name
        self.class_standing = class_standing
        self.exam_grade = exam_grade

    def calculate_grade(self):
        return 0.6 * self.class_standing + 0.4 * self.exam_grade

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "full_name": self.full_name,
            "class_standing": self.class_standing,
            "exam_grade": self.exam_grade
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            student_id=data["student_id"],
            full_name=data["full_name"],
            class_standing=data["class_standing"],
            exam_grade=data["exam_grade"]
        )

class RecordManagement:
    def __init__(self):
        self.records = []
        self.filename = None

    def load_file(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                self.records = [StudentRecord.from_dict(record) for record in json.load(file)]
            self.filename = filename
            print(f"Loaded records from {filename}")
        else:
            print("File does not exist.")

    def save_file(self):
        if self.filename:
            with open(self.filename, 'w') as file:
                json.dump([record.to_dict() for record in self.records], file)
            print(f"Records saved to {self.filename}")
        else:
            print("No filename specified. Use 'Save As' first.")

    def save_as_file(self, filename):
        self.filename = filename
        self.save_file()

    def show_all_records(self):
        for record in self.records:
            print(f"{record.student_id}: {record.full_name}, Class Standing: {record.class_standing}, Exam Grade: {record.exam_grade}")

    def order_by_last_name(self):
        self.records.sort(key=lambda record: record.full_name[1])
        print("Records sorted by last name.")

    def order_by_grade(self):
        self.records.sort(key=lambda record: record.calculate_grade(), reverse=True)
        print("Records sorted by grade.")

    def show_student_record(self, student_id):
        for record in self.records:
            if record.student_id == student_id:
                print(f"Record found: {record.student_id}: {record.full_name}, Class Standing: {record.class_standing}, Exam Grade: {record.exam_grade}")
                return
        print("Record not found.")

    def add_record(self, student_id, full_name, class_standing, exam_grade):
        if len(student_id) != 6 or not student_id.isdigit():
            print("Student ID must be a six-digit number.")
            return
        new_record = StudentRecord(student_id, full_name, class_standing, exam_grade)
        self.records.append(new_record)
        print("Record added.")

    def edit_record(self, student_id, class_standing=None, exam_grade=None):
        for record in self.records:
            if record.student_id == student_id:
                if class_standing is not None:
                    record.class_standing = class_standing
                if exam_grade is not None:
                    record.exam_grade = exam_grade
                print("Record updated.")
                return
        print("Record not found.")

    def delete_record(self, student_id):
        for record in self.records:
            if record.student_id == student_id:
                self.records.remove(record)
                print("Record deleted.")
                return
        print("Record not found.")

def main():
    management = RecordManagement()
    while True:
        print("\nMenu:")
        print("1. Open File")
        print("2. Save File")
        print("3. Save As File")
        print("4. Show All Students Record")
        print("5. Order by Last Name")
        print("6. Order by Grade")
        print("7. Show Student Record")
        print("8. Add Record")
        print("9. Edit Record")
        print("10. Delete Record")
        print("11. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            filename = input("Enter filename to open: ")
            management.load_file(filename)
        elif choice == '2':
            management.save_file()
        elif choice == '3':
            filename = input("Enter filename to save as: ")
            management.save_as_file(filename)
        elif choice == '4':
            management.show_all_records()
        elif choice == '5':
            management.order_by_last_name()
        elif choice == '6':
            management.order_by_grade()
        elif choice == '7':
            student_id = input("Enter Student ID: ")
            management.show_student_record(student_id)
        elif choice == '8':
            student_id = input("Enter Student ID (6 digits): ")
            full_name = tuple(input("Enter Full Name (First Last): ").split())
            class_standing = float(input("Enter Class Standing: "))
            exam_grade = float(input("Enter Exam Grade: "))
            management.add_record(student_id, full_name, class_standing, exam_grade)
        elif choice == '9':
            student_id = input("Enter Student ID to edit: ")
            class_standing = input("Enter new Class Standing (leave blank to keep current): ")
            exam_grade = input("Enter new Exam Grade (leave blank to keep current): ")
            class_standing = float(class_standing) if class_standing else None
            exam_grade = float(exam_grade) if exam_grade else None
            management.edit_record(student_id, class_standing, exam_grade)
        elif choice == '10':
            student_id = input("Enter Student ID to delete: ")
            management.delete_record(student_id)
        elif choice == '11':
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()