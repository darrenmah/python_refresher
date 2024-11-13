arr_test = [6,2,4,1,3]

# Grab pivot value
# Iterate through every single value of the input array except for pivot value 
# Every value less than or equal to the pivot value is in the left partition of the array
# Every value greater is on the right
# Partition can be done in place 
# Two Pointer
# If Comparison pointer is greater than our pivot value, move it over by 1, otherwise swap insertion pointer value with comparison pointer value then update insertion pointer 
# Insertion pointer is where we insert our value 
# Swap insertion pointer's value with the pivot index

#Pivot index is the ending index
#Insert pointer is the starting index

def quick_sort(arr, start, end):
    
    if end - start + 1 <= 1:
        return arr
    
    pivot_index = end
    insert_ptr = start

    #c for comparison pointer
    for c in range(start, end):
        if arr[c] < arr[pivot_index]:
            temp = arr[c]
            arr[c] = arr[insert_ptr]
            arr[insert_ptr] = temp
            insert_ptr += 1
   
    temp = arr[pivot_index]
    arr[pivot_index] = arr[insert_ptr]
    arr[insert_ptr] = temp

    #Quick Sort Left Side
    quick_sort(arr, start, insert_ptr - 1)

    #Quick Sort Right Side
    quick_sort(arr, insert_ptr + 1, end)

    return arr
    

    


test_arr = [5,6,7,1,2,3]
print(quick_sort(test_arr, 0, len(test_arr)-1))
#print(quick_sort(arr_test, 0, len(arr_test)-1))


