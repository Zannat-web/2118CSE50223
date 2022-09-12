class School_student:
    def __init__(self, Section, Result, Distict):
          self.Section = Section
          self.Result = Result
          self.Distict = Distict
    def display(self):
            print(self.Section)
            print(self.Result)
            print(self.Distict)

P1 = School_student("Science" ,3.17,"Dhaka,Doshaid Ak School")
P1.display()