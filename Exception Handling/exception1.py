"""
Write a program using try...except
"""

#__Main__
try:
    number1 = int(input("Enter first number "))
    number2 = int(input("Enter second number "))
    
    result = number1 // number2
    remainder = number1 % number2
    
    print("Quotient = ",result)
    print("Remainder = ",remainder)
except ValueError:
    print("Error: Enter valid number ")
except ZeroDivisionError:
    print("Error: Number divided by zero")
else:
    print("All numbers are valid")
finally:
    print("Control now at finally block")
    