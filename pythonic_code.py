#Python Unpacking
x_group = []
y_group = []

#Unpacking (multiple assignments to multiple variables)
x1, x2 = 100, 500
y1, y2 = 200, 450

print(x2 - x1)
print(y2 - y1)

#Unpacking lists of lists
coordinates = [[0,0],[1,1],[2,2],[3,3],[4,4],[5,5]]
for x, y in coordinates:
    print(f"X: is {x} and Y: is {y}")


#Enumeration - Get index and element in that index
nums = [1,2,3,4,5,6]

for index, value in enumerate(nums):
    print(index,value)

#Zip function - iterate over multiple lists at the same time

#Takes multiple lists and returns an iterator of tuples

list1 = [1,2,3,4,5,6,7,8]
list2 = ['Bob','Dave','Jill','Joe','John','Abe','Dan','Marvin']

for name, score in zip(list2, list1):
    print(f"{name} has a score of : {score}")





