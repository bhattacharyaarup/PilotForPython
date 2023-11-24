"""
Use of dictionary
"""
#__Main__
# Define a dictionary

dict = {'apple':150,'orange':200,'mango':80}
# Print dictionary
print(dict)
#Print each key value pair in seperate line, use loop over dictionary
print("\nList of key and value")
for key in dict:
    print(key,"=",dict[key])
    
#Iterate only over values
print("\nList of values")
for value in dict.values():
    print(value)
    
#Iterate over key:value pair using items() method
print("\nList using items() method")
for key,value in dict.items():
    print(key,"=",value)
    
print("\nLength of dictionary = ",len(dict))
print(max(dict.values()))
print(min(dict.values()))