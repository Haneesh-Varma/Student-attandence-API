class StudentData:
    def __init__(self,name,roll,present):
        self.name = name
        self.roll = roll
        self.present = present
    def getInfo(self):
        print(f"Name of the student: {self.name}")
        print(f"Roll no: {self.roll}")
        print(f"Attendance: {self.present}")

s1 = StudentData("Haneesh", 10, True)
s1.getInfo()
    
