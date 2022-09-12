class Collage_student:
    def __init__(self, Section, Result, Distict):
          self.Section = Section
          self.Result = Result
          self.Distict = Distict
    def display(self):
            print(self.Section)
            print(self.Result)
            print(self.Distict)

P1 = Collage_student("CSE" ,3.79,"Dhaka,Islami Bank Institute Of Technology.")
P1.display()