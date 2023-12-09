"""
Input 10 coordinates in a list of lists. Your task is to 
find the total distance from the first point to the last point.
"""
import math
points = []

for i in range(10):
    x = int(input("Enter value of x :"))
    y = int(input("Enter value of y :"))
    
    data = [x,y]
    points.append(data)
    
dist = 0
for i in range(len(points)-1):
    first = points[i]
    second = points[i+1]
    dist += math.sqrt(pow((first[0]-second[0]),2)+pow((first[1]-second[1]),2))
    
print("Total distance from first point to last point :",dist)