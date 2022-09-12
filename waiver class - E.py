class Grade_Calculator:
    def __init__(self, ID, GPA1,GPA2,GPA3):
          self.ID= ID
          self.GPA1 = GPA1
          self.GPA2 = GPA2
          self.GPA3 = GPA3
    def Count_CGPA (self):
     return(self.GPA1+self.GPA2+self.GPA3)/3
    def Display(self):
            print(f"student's ID:{self.ID}")
            print(f"CGPA:{self.Count_CGPA():2f}")

P1 = Grade_Calculator(50223,3.56,2.81,3.19)
cgpa=Grade_Calculator.Count_CGPA()
            print(f"{CGPA:.2f}")
P1.Display()