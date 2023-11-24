"""
Use of custom module
"""
import mymodule

number = int(input("Enter a number :"))
flag = mymodule.check(number)
if flag:
    print("Number is even")
else:
    print("Number is odd")
    

