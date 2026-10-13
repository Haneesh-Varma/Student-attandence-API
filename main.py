class Student:
    def __init__(self,name,roll,attendance):
        self.name = name
        self.roll = roll
        self.attendance = attendance
def get_info(students,roll):
    student = find_student(students,roll)
    print(f"Name of the student: {student.name}")
    print(f"Roll no: {student.roll}")
    print(f"Attendance: {student.attendance}")

def find_student(students,roll):
    for student in students:
        if student.roll == roll:
            return student
    return None
def mark_attendance(students,roll,attendance):
    student = student = find_student(students,roll)
    student.attendance = True
def add_student(students,name,roll,attendance):
    if find_student(students,roll):
        print("Error student aleardy exists")
        return
    students.append(Student(name,roll,attendance))
    print("Student added.")


students = []
add_student(students,"Haneesh", 10, True)
add_student(students,"Salman", 11, True)
add_student(students,"Mokshith", 12, False)
add_student(students,"Rd",13,False)
get_info(students,10)
student = find_student(students,11)
if student is not None:
    print(student.name)
else:
    print("No student found")

mark_attendance(students,12,True)
get_info(students,12)
