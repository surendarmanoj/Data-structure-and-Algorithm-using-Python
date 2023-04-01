import math

x = []
start = 0

for i in range(2000):
    x.append(i)
print(x)
print(len(x))
print("======================")
end = len(x) - 1
target = 1999

def binarysearch(iplist, start, end, target):
    print(x[start:end+1])
    print("_______________________________________________________________________________________________________________")
    if start > end:
        return False
    midIndex = math.floor((start + end)/2)
    if(x[midIndex] == target):
        return True
    elif(x[midIndex] > target ):
        return binarysearch(iplist,start, midIndex -1, target)
    else:
        return binarysearch(iplist, midIndex + 1, end, target)


print(binarysearch(x, start, end, target))