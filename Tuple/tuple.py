"""
Handling tuple in Python
"""
city = ('Kolkata','Mumbai','Delhi','Chennai')
print(city)
print(city[1:3])

'''
Tuple is immutable data type
city [1] = 'Patna'
This statement throw an error called TypeError
To modify tuple, use the help of list
'''

cityList = list(city)
cityList[1]='Patna'
city = tuple(cityList)

print(city)

for index in range(len(city)):
    print(city[index])
    
for index in range(-1, -(len(city)+1),-1):
    print(city[index])
    