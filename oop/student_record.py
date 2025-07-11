class Student:
    counter = 0

    def __init__(self):
        self.name = ""
        self.roll_no = ""
        self.grades = {}
        self.avg_grade = 0

        Student.counter += 1
        self.__menu()
        
    
    @staticmethod
    def count_student():
        print(f"Total record created: {Student.counter}")

    def __str__(self):
        return f"Student (Name: {self.name}, Roll No: {self.roll_no}, Avg Grade: {self.avg_grade}"
    
    def __menu(self):
        while True:
            print("""
                Which operation you want to do?
                1. Add student name
                2. Add student roll no
                3. Add student grades
                4. Calculate average grade point
                5. Print student details
                6. Exit
    """)
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_name()
            elif choice == "2":
                self.add_roll_no()
            elif choice == "3":
                self.add_grade()
            elif choice == "4":
                self.average_grade()
            elif choice == "5":
                self.student_details()
            elif choice == "6":
                print("Operation closed. Thank you!")
                break
            else:
                print("Invalid input! Please enter a number from 1 to 6!")
    
    def add_name(self):
        self.name = input("Enter student name: ")
        print("\nStudent name is successfully added!")
    
    def add_roll_no(self):
        self.roll_no = input("Enter student roll_no: ")
        print("\nStudent roll no is successfully added!")
    
    def add_grade(self):
        subject = input("Enter subject name: ")
        try:
            grade = float(input("Enter grade point: "))
            self.grades[subject] = grade
            print(f"\nGrade {grade} is added for {subject}!")
        except ValueError:
            print("Invalid grade input!")
    
    def average_grade(self):
        if len(self.grades) > 0:
            self.avg_grade = round(sum(self.grades.values()) / len(self.grades), 2)
            print(f"\nAverage grade of {self.name} is {self.avg_grade}")
        else:
            print("\nNo grade is available!")
    
    def student_details(self):
        print("\nStudent Details:")
        print(f"Name: {self.name}")
        print(f"Roll no: {self.roll_no}")
        print(f"Average Grade: {self.avg_grade}")
        print(f"Grades: {self.grades}")

if __name__ == "__main__":
    student1 = Student()
    Student.count_student()

    
