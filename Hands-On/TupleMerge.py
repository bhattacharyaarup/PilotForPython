"""
Write a program that inputs two tuples and creates a third tuple that contains
all the elements of the first tuple and the unique value from the second tuple. 
Print the new tuple.
"""
tup1 = eval(input("Enter value for the first tuple "))

tup2 = eval(input("Enter value for te second tuple "))

# Merge two tuples with the help of list
# Convert tuple to list
tempList1 = list(tup1)
tempList2 = list(tup2)

# Check whether an element of second list is present in the first list
# If not present, append it to the end  of the first list
for value in tempList2:
    if value in tempList1:
        continue
    else:
        tempList1.append(value)
        
# Create new tuple and store data from the first list
tup3 = tuple(tempList1)
print("First tuple: ",tup1)
print("Second tuple: ",tup2)
print("Merged tuple ",tup3)
