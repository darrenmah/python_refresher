list_comp = [i for i in range(5)]
print(list_comp)

list_comp = [i*i for i in range(5)]
print(list_comp)

#List comprehension using zip function
arr1 = [1,2,3]
arr2 = [4,5,6]
list_comp2 = [i+j for i, j in zip(arr1, arr2)]
print(list_comp2)


arr_condition = [2,4,6,7,8,10]
list_comp3 = [i for i in arr_condition if i % 2 == 0 ]
print(list_comp3)

