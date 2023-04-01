from collections import deque

mystack = deque()
list1 = [1,2,3,4,5,6,7,8,9]


for i in list1:
    mystack.append(i)
    print(mystack)
print("\n")

for i in mystack:
    print(i, end = " ")
print("\n")



mystack.pop()
for i in mystack:
    print(i, end = " ")
print("\n")

