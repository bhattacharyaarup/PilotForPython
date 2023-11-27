# Example of multiple inheritance
# Define Employee class
class Employee:
    #Define constructor
    def __init__(self, id, ename):
        self.id = id
        self.ename = ename

    #Function to display information
    def showInfo(self):
        print("ID =", self.id, "Name of employee =", self.ename)

# Define Programmer class inherited from Employee class
class Programmer(Employee):
    #Define constructor
    def __init__(self, id, ename, language):
        Employee.__init__(self,id, ename)
        self.language = language

    #Function to display information
    def showInfo(self):
        super().showInfo()
        print("Development Language =", self.language)

# Define Manager class inherited from Employee class
class Manager(Employee):
    #Define constructor
    def __init__(self, id, ename, department):
        Employee.__init__(self,id, ename)
        self.department = department

    #Function to display information
    def showInfo(self):
        super().showInfo()
        print("Department =", self.department)

# Define Development Manager class using Multiple inheritances
class DevManager(Manager,Programmer):
    #Define constructor
    def __init__(self, id, ename, language, department):
        # Multiple inheritance requires explicit initialization
        Programmer.__init__(self, id, ename, language)
        Manager.__init__(self, id, ename, department)

    #Function to display information
    def showInfo(self):
        print("\nEmployee Information\n")
        super().showInfo()

# Main
#Check MRO of class DevManager
print("\nMethod resolution order of DevManager class\n")
print(DevManager.mro())
# Create an instance of DevManager class
obj = DevManager("A101", "Rajib Menon", "Python", "Engineering")
obj.showInfo()



