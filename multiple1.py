"""
Multiple Inheritance
"""
# First base class
class Student:
    
    # Constructor to initialize member variable
    def __init__(self, studentName):
        self.studentName = studentName
        
    # Display the information
    def display(self):
        print("Name of student : ",self.studentName)
        
# Second base class
class Marks:
    
    # Constructor to initialize member variable
    def __init__(self, marks1, marks2):
        self.marks1 = marks1
        self.marks2 = marks2
        
    # Display the information
    def display(self):
        print("Marks obtained : ",self.marks1,self.marks2)
        
# Create inherited class from Student and Marks class
class Science(Student, Marks):
    
    # Constructor for initialize both the class member variable
    # Multiple inheritance requires explicit initialization
    def __init__(self, studentName, marks1, marks2):
        Student.__init__(self,studentName)
        Marks.__init__(self,marks1, marks2)
        
    # Display students information from both the classes
    def display(self):
        Student.display(self)
        Marks.display(self)
        
#__Main__
# Create an object of the Science class
obj = Science('Amit Agarwal',78,89)
obj.display()
