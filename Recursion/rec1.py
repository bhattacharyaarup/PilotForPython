"""
Input a number and check whether it is a Prime number
or not using recursion.
"""

#Define recursive function
def isPrime(number, factor):
    if number == 1:
        return False
    if factor > number / 2:
        return True
    else:
        if number % factor == 0:
            return False
        else:
            return isPrime(number, factor + 1)
        
#__Main__
#Accept a number
number = int(input("Enter a number "))
factor = 2
flag = isPrime(number, factor)
if flag == True:
    print(number,"is Prime")
else:
    print(number, "is not prime")
    
    