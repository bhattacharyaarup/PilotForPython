"""
Binary File handling in Python
"""
# Import pickle module for binary file handling
import pickle

# Open file in write binary bode
file = open("data.dat","wb")

# Create an infinite loop till user wants to terminate
while(True):
    # Enter data from user to store into file
    id = int(input("Enter id: "))
    studentName = input("Enter name of student: ")
    total = int(input("Enter total marks of the student: "))
    
    # Create a dictionary object to store data
    data = {"id":id, "studentName":studentName,"total":total}
    # Using dump method of pickle module store dictionary object
    pickle.dump(data, file)
    
    resp = input("Want to add any more Y/N ")
    if resp =='y' or resp=='Y':
        continue
    else:
        break
    
# Close the binary file after storing data
file.close()

# Open file in read binary mode
file = open("data.dat","rb")

# Exception handling till end of file
try:
    while(True):
        
        # Using load method of pickle module read data into dictionary object
        data = pickle.load(file)
        print(data)
except EOFError:
    print("End of file read.")
    
# Close the binary file after reading was completed
file.close()