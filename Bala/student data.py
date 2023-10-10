class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

    def __str__(self):
        return f"Name: {self.name}, Roll Number: {self.roll_number}, CGPA: {self.cgpa}"

def sort_students(student_list):
    # Sort the list of students based on CGPA in descending order
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Test the function with different input lists of students
if __name__ == "__main__":
    students1 = [
        Student("Bala", "A001", 3.9),
        Student("Pradeep", "B002", 3.7),
        Student("Ruban", "C003", 4.0),
    ]

    students2 = [
        Student("Sanjai", "D004", 3.8),
        Student("Hari", "E005", 3.5),
        Student("Muthu", "F006", 3.9),
    ]

    sorted_students1 = sort_students(students1)
    sorted_students2 = sort_students(students2)

    print("Sorted Students 1:")
    for student in sorted_students1:
        print(student)

    print("\nSorted Students 2:")
    for student in sorted_students2:
        print(student)
