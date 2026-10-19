from flask import Flask
from main import Student, get_info, add_student, mark_attendance, find_student

students = []
add_student(students,"Haneesh", 10, True)
add_student(students,"Salman", 11, True)
add_student(students,"Mokshith", 12, False)
add_student(students,"Rd",13,False)

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Student Attendance API is running!"}

@app.route("/about")
def about():
    return {"message": "Our Student Attendance API makes attendace systems smooth and seamless for institutional benchmarks"}
@app.route("/info/<int:roll>")
def get_student(roll):
    student = find_student(students,roll)
    if student is None:
        return{"Error: " : "Student does not exist in the database."},404
    return{
           "Name: " : student.name,
           "Roll no: " : student.roll,
           "Attendance: " : student.attendance
           },200


if __name__ == "__main__":
    app.run(debug=True)