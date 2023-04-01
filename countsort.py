arr = [2,1,2,6,0,4,3,3]

def countsort(arr):
    l = max(arr)+1
    n = len(arr)
    res = [0] * n
    c = [0] * l
    print(res)

    for i in range(0,n):
        c[arr[i]] = c[arr[i]] + 1

    for j in range(1,len(c)):
        c[j] = c[j] + c[j-1]

    print(c)

    k = n-1
    while k >= 0:
        res[c[arr[k]]-1] = arr[k]
        c[arr[k]] -= 1

        k -= 1
    
    return res

print(countsort(arr))