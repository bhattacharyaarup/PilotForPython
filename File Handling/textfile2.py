"""
Text file handling with tell and seek method
"""

file = open("players.txt","r")
line = file.readline()
print(line)
print("Read pointer after read=",file.tell())

# If you want to print this first line once again, set pointer at 0
file.seek(0)
line = file.readline()
print("Line from file after setting pointer at zero")
print(line)

file.close()
