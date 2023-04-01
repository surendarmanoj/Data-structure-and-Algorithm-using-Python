arr = [23,29,15,19,31,7,9,5,2]

def quicksort(arr):

    gap = len(arr)//2

    while gap > 0:
       

        for i in range(gap, len(arr)):

            cur = arr[i]
            prev = i

            while prev >= gap and cur < arr[prev - gap]:
                arr[prev], arr[prev-gap] = arr[prev-gap], arr[prev]
                prev = prev - gap

            arr[prev] = cur

        gap = gap // 2
        print(arr)

quicksort(arr)
