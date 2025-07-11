class Student:
    def __init__(self):
        self.name = ""
        self.roll_no = ""
        self.grades = {}

        self.__menu()

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
                print("Operation is closed!")
                break
            else:
                print("Invalid input! Please enter 1-5!")
    
    def add_name(self):
        self.name = input("Enter student name: ")
        print("Student name is successfully added!")
    
    def add_roll_no(self):
        self.roll_no = input("Enter student roll_no: ")
        print("Student name is successfully added!")
    
    def add_grade(self):
        subject = input("Enter subject name: ")
        grade = int(input("Enter grade point: "))
        self.grades[subject] = grade
        print(f"Grade {grade} is added for {subject}!")
    
    def average_grade(self):
        return (sum(self.grades.values()) / len(self.grades))
    
    def student_details(self):
        print(f"Name: {self.name}")
        print(f"Roll no: {self.roll_no}")
        print(f"Average Grade: {average_grade(self)}")
    
