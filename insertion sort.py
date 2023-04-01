arr = [2,56,31,67,10,4,8,100,32,42]

for i in range(0,len(arr)):
    cur = arr[i]
    for j in range(i-1, -1, -1):
        if arr[j] > cur:
            arr[j+1] = arr[j]
        else:
            arr[j+1] = cur
            break

    print(arr)