"""
Design a Python application to obtain a search criteria from user 
and then fetch records based on that from empl table.
Empl 
empno     integer
ename     varchar
job       varchar
salary    integer
allowance integer
dept_code integer
"""

# Import package 
import mysql.connector

# Open connection to MySQL database
mycon = mysql.connector.connect(host = "localhost",
                                user = "root",
                                password = "admin",
                                database = "alphabetz")

# Create a cursor object
mycursor = mycon.cursor()
# Accept employee name from user
ename = input("Enter employee name :")
# Execute query to search given name
mycursor.execute("select * from empl where ename='"+ename+"'")
# Get all record from cursor object
records = mycursor.fetchall()

found = False
# Create a loop over all records
for record in records:
    print("Emp. No      :"+str(record[0]))
    print("Emp. Name    :"+record[1])
    print("Job Title    :"+record[2])
    print("Basic Salary :"+str(record[3]))
    print("Allowance    :"+str(record[4]))
    print("Dept Code    :"+str(record[5]))
    found = True
    
# If name is not found print appropriate message
if found == False:
    print("Name not found...")
    
# Close all open connection
mycursor.close()
mycon.close()