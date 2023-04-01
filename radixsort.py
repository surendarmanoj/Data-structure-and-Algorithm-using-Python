arr = [423, 324, 123,5,725]

def CountingSort(arr, p):
    n1 = len(arr)
    res = [0] * n1
    c = [0] * 10

    for i in range(0,n1):
        temp = arr[i] // p
        c[temp%10] += 1
        # print(c)

    for j in range(1, 10):
        c[j] = c[j] + c[j-1]

    k = n1 - 1

    while k>=0:
        t1 = arr[k] // p
        
        res[c[t1%10] - 1 ] = arr[k]
        c[t1%10] -= 1
        k = k- 1
    
    print(res)

    

def Radixsort(arr):
    maximum = max(arr)
    n = 1
    while maximum // n > 0:
        CountingSort(arr, n)
        n = n*10

print(arr)
print("_________________________")
Radixsort(arr)
