class University_student:
    def __init__(self, Semester, Current_CGPA):
          self.Semester = Semester
          self.Current_CGPA = Current_CGPA

    def display(self):
            print(self.Semester)
            print(self.Current_CGPA)


P1 = University_student('3rd' ,3.19)
P1.display()