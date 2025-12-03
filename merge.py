def merge_sort(arr):
    mid = len(arr) // 2
    if len(arr)>1:
        l_arr = arr[:mid]
        r_arr = arr[mid:]

        merge_sort(l_arr) #to sort the left sub array
        merge_sort(r_arr) #to sort the right sub array


        i=0 #for left sub array
        j=0 #for right sub array
        k=0 #for the main merged array

        while i < len(l_arr) and j< len(r_arr):
            if l_arr[i] < r_arr[j]:
                arr[k] = l_arr[i]
                i += 1

            else:
                arr[k] = r_arr[j]
                j += 1
            k += 1

        while i<len(l_arr):
            arr[k] = l_arr[i]
            i += 1
            k += 1

        while j<len(r_arr):
            arr[k] = r_arr[j]
            j += 1
            k += 1

test_arr = [3,4,8,7,4,5,9,1,9,0] #for testing
merge_sort(test_arr)
print(test_arr)
 
