"""
Example program of multilevel inheritance
"""

# Define base class
class Student:
    # Constructor to initialize name of a student
    def __init__(self, name):
        self.name = name
    
    # Display information of a student
    def display(self):
        print("Name of student : ",self.name)
        
# Defind derived class from Student class
class Marks(Student):
    
    # Define constructor to initialize name, first subject marks
    # and second subject marks
    def __init__(self,name, subj1, subj2):
        super().__init__(name)
        self.subj1 = subj1
        self.subj2 = subj2
        
    # Display information of a student
    def display(self):
        super().display()
        print("Marks in 1st subject : ",self.subj1)
        print("Marks in 2nd subject : ",self.subj2)
        
# Define derived class from Marks class
class Result(Marks):
    # Constructor to initialise member variable and total with zero
    def __init__(self, name, subj1, subj2):
        super().__init__(name, subj1, subj2)
        self.total = 0
        
    # Calculate total marks
    def calculate(self):
        self.total = self.subj1 + self.subj2
        
    # Display information of a student
    def display(self):
        super().display()
        print("Total marks : ",self.total)
        
#__Main__
# Create an object of Result class
obj = Result('Rajeev',80, 90)
# Invoke calculate function to calculate total marks
obj.calculate()
# Display information
obj.display()