class student:
    def __init__(self, Name, ID, Institute):
          self.Name = Name
          self.ID = ID
          self.Institute = Institute
    def display(self):
            print(self.Name)
            print(self.ID)
            print(self.Institute)
P1 = student("Zannat",223,"MIU")
P1.display()