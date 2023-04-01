arr = [2,56,31,67,10,4,8,100,32,42]

for j in range(0, len(arr)):
    swap = 0
    for i in range(0, len(arr)-1):
        if arr[i] > arr[i+1]:
            arr[i],arr[i+1] = arr[i+1], arr[i]
            swap += 1
    print(arr,swap)
    if swap == 0:
        break