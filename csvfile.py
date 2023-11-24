"""
Create and read a csv file
"""

import csv
# Open file in write mode 
file = open("student.csv",'w', newline='\n')
#Create writer object for the file
mywriter = csv.writer(file)
# Define header row
row = ['Name','Address','State']
# Write header row
mywriter.writerow(row)
#Create a loop till user wants to stop
while(True):
    name = input("Enter name ")
    address = input("Enter address ")
    state = input("Enter state ")
    
    #Add data to the list object row
    row=[name,address,state]
    #Write each row into the file
    mywriter.writerow(row)
    
    resp = input("Want to continue Y/N ");
    if(resp =='y' or resp=='Y'):
        continue
    else:
        break
    
#Close the file 
file.close()
#Open file in read mode
file = open("student.csv","r",newline='\n')
#Create reader object for the file
myreader = csv.reader(file)
#Create a loop over the reader object, and extract each row
#in the reacrod list object
for record in myreader:
    print(record)
    
#Close the file
file.close()
