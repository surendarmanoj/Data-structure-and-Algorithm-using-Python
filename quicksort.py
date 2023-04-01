arr = [22,11,88,55,77,33,44]

def quicksort(arr, start, end):
    if start < end:
        partition_index = partition(arr, start, end)
        quicksort(arr, start, partition_index-1)
        quicksort(arr, partition_index+1, end)
        print(arr)



def partition(arr, start, end):
    i = start
    j = end-1
    pivot = arr[end]

    while i < j:
        while arr[i] < pivot and i < end:
            i += 1
        while arr[j] >= pivot and j >start:
            j -= 1

        if i < j:
            arr[i],arr[j] = arr[j], arr[i]
    
    if arr[i] > pivot:
        arr[i], arr[end] = arr[end], arr[i]
    
    return i

print(arr)
quicksort(arr, 0, len(arr)-1)
print(arr)