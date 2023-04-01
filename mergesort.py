arr = [15,5,24,8,1,3,16,10,20]

def mergeSort(arr):
    #divide
    if len(arr) > 1:
        mid = len(arr)//2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
       
        #recursive split of arrays
        mergeSort(left_arr)
        mergeSort(right_arr)

        #merge
        i = 0
        j = 0
        k = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j+= 1

            k += 1
           
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i+=1
            k+=1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j+=1
            k+=1
    print(arr)
    print("------------------------------")
    
mergeSort(arr)