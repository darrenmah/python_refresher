#Python Strings

#Getting Length of a String using len()
print(len("This is my string."))

#String Slicing - allows us to access substrings of strings
my_string = "Hello World"
start = 1
end = 5
print(my_string[1:5])
#Goes from index 1 to index 4 (not including 5)

my_string = "ABCD"
print(my_string[:3])
print(my_string[0:3])
print(my_string[2:])

#String reversal
reverse = my_string[::-1]
print(reverse)

#Python strings are immutable, we cannot change after they have been created. We have to reassign
#We have to slice and concatenate to remove characters


#Python Function Type Hints
#Doesn't affect whether the function accepts whats being passed in or not
def add(x: int, y: int):
    return x + y


#Python Lists
my_list = [1,2,3,4,5,6]
#Lists are mutable

if 2 in my_list:
    print('2 is in this list')

if 7 not in my_list:
    print('7 is not in this list')

#List looping 

for i in range(len(my_list)):
    print(my_list[i])

for num in my_list:
    print(num)


#List Functions (Sum, Min, Max of the List Items)
print(sum(my_list))
print(min(my_list))
print(max(my_list))

my_list.append(7)
print(my_list)

#Remove from end of list
my_list.pop()

#Remove from specific index
my_list.pop(0)

print(my_list)

#Get an index of a certain element

find_list = [1,2,3,4,5,6,7,8,9,10,999,12,13,14,15]

print(find_list.index(999))


#List Slicing
print(my_list[:3])
print(my_list[1:])
print(my_list[::-1])

#Tuples are like lists but they are immutable
my_tuple = (1,2,3,4)
print(my_tuple[0])

#Sets are unordered
set_values = {1,2,3,4,5,6}

if 5 in set_values:
    print('5 in the set ')

empty_set = set()
print(empty_set)
empty_set.add(1)
print(empty_set)



#Python Dictionaries
dictionary = {"a": 1, "b": 2}

for key in dictionary:
    value = dictionary[key]
    print(key,value)


#Removing from dictionary
dictionary.pop("a")
dictionary.pop("b")

