elements = [1,2,3,4,5]
elements.append(6)
elements.pop()
elements.pop(4)
elements.insert(4,1000)
print(elements)
print(elements.index(4))
elements2 = [6,7,8,9,10]
elements2.remove(10)
elements = [1,2,3,4,5]
elements.extend(elements2)
print(elements)
print(elements2)

#List concatenation 
full_num_list = [1,2,3,4,5] + [6,7,8,9,10,11,12]
print(full_num_list)

#List initialization - Creating an empty list of 5 elements 
my_list = [0] * 5

print(my_list)

original_list = ['a','b','c','d']
clone = original_list.copy()
print(clone)
clone = original_list[1:]
print(clone)

#List Comprehension - allows us to create lists in a concise way 



