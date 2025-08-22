class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display_details(self):
        print("----- Student Details -----")
        print(f"Name        : {self.name}")
        print(f"Roll Number : {self.roll_number}")
        print(f"Marks       : {self.marks}")
        print("---------------------------")

name = input("Enter student name: ")
roll_number = input("Enter roll number: ")
marks = input("Enter marks: ")

student1 = Student(name, roll_number, marks)
student1.display_details()