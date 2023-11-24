"""
Single Inheritance
"""

# Define base class
class Student:
    
    # Define constructor
    def __init__(self, roll, studentName):
        self.roll = roll
        self.studentName = studentName
        
    # Display the student information
    def display(self):
        print("Roll number : ",self.roll)
        print("Name : ",self.studentName)
        
# Define derived class from Student class
class Marks(Student):
    
    # Define constructor
    def __init__(self,roll,studentName,marks1,marks2):
        super().__init__(roll, studentName)
        self.total = 0
        self.marks1 = marks1
        self.marks2 = marks2
        
    # Function to calculate total marks
    def calculate(self):
        self.total = self.marks1 + self.marks2
        
    # Display information of a student
    def display(self):
        super().display()
        print("Marks obtained : ",self.marks1,",",self.marks2)
        print("Total marks : ",self.total)
        
#__Main__
# Create an object of Marks class
obj = Marks(101, 'Amit Khurana', 78,88)
obj.calculate()
obj.display()