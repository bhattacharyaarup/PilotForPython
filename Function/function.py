"""
Handling function in Python
"""

# Function with no parameter and no return type
def welcome():
    print("Welcome to function")
    
# Function with parameter
def addition(number1, number2):
    result = number1 + number2
    print("Sum = ",result)
    
# function with return value
def multiply(number1, number2):
    prod = number1 * number2
    return prod

# Function with default value
def area(length, breadth=10):
    ar = length * breadth
    print("Area = ",ar)
    
# Function with multiple return statements
def calculation(number1, number2):
    result = number1 + number2
    avg = result / 2
    return result, avg

#__Main__
welcome()

addition(10,12)

print("Product=",multiply(10,12))

# Call function with the value of length
area(5)
# Call function with the positional value of length and breadth
area(5,7)
# Call function with the keyword argument for length and breadth
area(breadth=2, length=5)

# Return as a tuple
value = calculation(10,12)
print(value)

# Return in two different variables
x, y = calculation(10,12)
print("Sum=",x)
print("Average=",y)
