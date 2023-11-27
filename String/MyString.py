"""
String handling in Python
"""

message = "welcome to alphabetz"

print("Length of the string = ",len(message))

print("Capitalized message = ",message.capitalize())

print("Number of letter e present = ",message.count('e', 0))

print("Number of letter e present upto 10th index = ",message.count('e', 0, 10))

print("Index of letter l = ", message.find('l'))

print("Index of the letter l from the 5th index ",message.find('l', 5))

print("Index of letter x ", message.find('x'))

print("Index of letter l ", message.index('l'))

print("Index of letter l from 5th index ", message.index('l',5))

'''
Index function returns first index, if not found it will
return exception value raised
print("Index of letter x ", message.index('x'))
'''

value1 = 'Kolkata34'
value2 = '45'
value3 = 'hello'

print(value1, 'is alphanumeric=',value1.isalnum())
print(value2, 'containing all digits =', value2.isdigit())
print(value1, 'containing all digits =',value1.isdigit())
print(value3, 'in all upper case =',value3.isupper())
print(value3, 'in all lower case =', value3.islower())
print(value1, 'change to lower case =',value1.lower())
print(value1, 'change to upper case =', value1.upper())

value4 = "   "
print("All characters are spaces =",value4.isspace())

value5 = "           welcoem to python         "
print("Remove spaces from the left side =[",value5.lstrip(),"]")
print("Remove spaces from right side =[", value5.rstrip(),"]")
print("Remove spaces from both end =[",value5.strip(),"]")

print("Starts with wel word =",message.startswith('wel'))
print("Starts with done word =",message.startswith('done'))
print("Ends with betz word =",message.endswith('betz'))
print("Ends with wel word =",message.endswith('wel'))

print(message, "convert to title case =",message.title())
message = message.replace("alphabetz", "Python")
print("Message after replace =", message)

mylist = ['12', '07', '2023']
greet = "/".join(mylist)
print("After joining using / as a seperator =",greet)

mylist1 = message.split()
print("Message splitting by blank space =",mylist1)

text = "welcome to alphabetz learn python"
mylist2 = text.split("alphabetz")
print("Message splitting by alphabetz word =", mylist2)

mytup = text.partition("alphabetz")
print("Message partition by alphabetz word =",mytup)