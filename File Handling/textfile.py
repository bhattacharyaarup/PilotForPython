"""
Text file handling in Python
"""

# Open file in write mode
file = open("players.txt","w")
while(True):
    line = input("Enter indian players name: ")
    # Using write method store line into file
    file.write(line+"\n")
    
    resp = input("Want to add more Y/N ")
    if(resp == 'y' or resp == 'Y'):
        continue
    else:
        break
    
# Close the file after write was complete
file.close()

#Open file in read mode
file = open("players.txt","r")
line = " "
print("Using readline method")
while line:
    line = file.readline()
    print(line,end="")
    
file.close()

#Open file in read mode
file = open("players.txt","r")
print("Using read method")
line = file.read()
print(line)
file.close()

#Open file in read mode
file = open("players.txt","r")
print("Using readlines method")
line = file.readlines()
print(line)
file.close()