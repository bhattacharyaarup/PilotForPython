"""
Custom exception handling
"""
# Define custom exception class inherited
# from Exception class
class MyException(Exception):
    
    # Constructor to set error message
    def __init__(self, message):
        self.message = message
        
#Define our program where custom exception
#will be handled. If number is negative then
#Custom exception will be raised.
try:
    num = int(input("Enter a positive number "))
    #Check for negative number
    if num < 0:
        raise MyException("Number is negative.")
    remainder = 100 % num
    if remainder == 0:
        print("Number is a factor of 100")
    else:
        print("Number is not a factor of 100")
#except block for input other than number
except ValueError:
    print("Invalid number")
#If number is divided by zero
except ZeroDivisionError:
    print("Number is not divided by zero")
#If the number is negative, custom error will raise
except MyException as error:
    print("Error: ",error)
    
    
