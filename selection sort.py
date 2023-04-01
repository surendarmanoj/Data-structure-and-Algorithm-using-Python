arr = [2,56,31,67,10,4,8,100,32,42,1]

for j in range(len(arr)):
    smallest = arr[j]
    smallest_index = j
    for i in range(j+1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    arr[j], arr[smallest_index] = arr[smallest_index], arr[j]
    print(arr)