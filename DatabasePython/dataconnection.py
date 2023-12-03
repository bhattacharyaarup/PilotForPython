"""
Python with MySQL
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

# Execute SQL Query
mycursor.execute("select * from student")

# Extract data from ResultSet
records = mycursor.fetchall()
for row in records:
    print(row)
    
# Close cursor and connection
mycursor.close()
mycon.close()
