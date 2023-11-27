# Example of hierarchical inheritance
# Define Employee class
class Employee:
    #Define constructor with employee id and employee name
    def __init__(self, id, ename):
        self.id = id
        self.ename = ename

    #Function to display information of an employee
    def showInfo(self):
        print("\nID =", self.id, "Name of employee =", self.ename)


# Define Programmer class inherited from Employee class
class Programmer(Employee):
    #Define constructor with employee id, name and language known
    def __init__(self, id, ename, language):
        Employee.__init__(self,id, ename)
        self.language = language

    #Function to display information of an employee
    def showInfo(self):
        super().showInfo()
        print("Development Language =", self.language)


# Define Manager class inherited from Employee class
class Manager(Employee):
    #Define constructor with employee id, name and department of an employee
    def __init__(self, id, ename, department):
        Employee.__init__(self,id, ename)
        self.department = department

    #Function to display information of an employee
    def showInfo(self):
        super().showInfo()
        print("Department =", self.department)
        
        
#__Main__
#Create an object of Prgrammer class
obj1= Programmer('A101',' Raman Srikant','Java')

#Create an object of Manager class
obj2 = Manager('B101','S Srinivashan','Sales')

#Display information from two objects
obj1.showInfo()
obj2.showInfo()


