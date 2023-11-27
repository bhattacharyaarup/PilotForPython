"""
List manipulation in Python
"""
 
city = ['Kolkata', 'Delhi', 'Mumbai', 'Chennai']
print(city)
print(city[1:3])

for item in city:
    print(item)

city[1]='Patna'
print(city)
print("Forward indexing")
for index in range(len(city)):
    print(city[index])
    
print("Backward indexing")
for index in range (-1, -(len(city)+1),-1):
    print(city[index])
    
result = [['A Kumar','S Pal','D Dey'],[23,278,256]]
print("Nested list")
print(result)
print("Each row")
for row in range(len(result)):
    print(result[row])
    


