def merge_sort(arr):

    if len(arr) == 1:
        return arr

    middle = len(arr)//2
    left_sub = merge_sort(arr[:middle])
    right_sub = merge_sort(arr[middle:])

    #Pointers for left and right subarray comparison
    left_ptr, right_ptr = 0, 0

    #Sorted array 
    sorted_array = [0]*len(arr)
    sorted_array_index = 0

    while left_ptr < len(left_sub) and right_ptr < len(right_sub):
        if left_sub[left_ptr] < right_sub[right_ptr]:
            sorted_array[sorted_array_index] = left_sub[left_ptr]
            left_ptr += 1
                
        else:
            sorted_array[sorted_array_index] = right_sub[right_ptr]
            right_ptr += 1
            
        sorted_array_index += 1
    
    

        #Excess elements should be handled left to right 
    while left_ptr < len(left_sub):
        sorted_array[sorted_array_index] = left_sub[left_ptr]
        left_ptr += 1
        sorted_array_index += 1
        
    while right_ptr < len(right_sub):
        sorted_array[sorted_array_index] = right_sub[right_ptr]
        right_ptr += 1
        sorted_array_index += 1
        

    return sorted_array
    
arr_test = [5,6,1,9,12,3]

print(merge_sort(arr_test))




