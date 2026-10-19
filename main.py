class Student:
    def __init__(self,name,roll,attendance):
        self.name = name
        self.roll = roll
        self.attendance = attendance

def get_info(students,roll):
    student = find_student(students,roll)
    if student is None:
        print("Student not found")
        return 0
    print(f"Name of the student: {student.name}")
    print(f"Roll no: {student.roll}")
    print(f"Attendance: {student.attendance}")
def find_student(students,roll):
    for student in students:
        if student.roll == roll:
            return student
    return None
def mark_attendance(students, roll, attendance):
    student = find_student(students, roll)
    if student is None:
        print("Student not found")
        return 0
    student.attendance = attendance
    return 1
def add_student(students,name,roll,attendance):
    if find_student(students,roll):
        print("Error: student aleardy exists")
        return 0
    students.append(Student(name,roll,attendance))
    return 1


students = []
add_student(students,"Haneesh", 10, True)
add_student(students,"Salman", 11, True)
add_student(students,"Mokshith", 12, False)
add_student(students,"Rd",10,False)
get_info(students,10)
student = find_student(students,11)
if student is not None:
    print(student.name)
else:
    print("No student found")

mark_attendance(students,16,True)
get_info(students,15)
