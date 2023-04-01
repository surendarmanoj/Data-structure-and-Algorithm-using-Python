class Node:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.next = next


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

e = Node(5)
f = Node(6)
g = Node(7)
h = Node(8)
i = Node(9)

a.next = b
b.next = c
c.next = d
d.next = e

e.next = f
f.next = g
g.next = h
h.next = i

def zipperlist(head1, head2):

    if head1 == None and head2== None : return None
    if head1 == None : return head2
    if head2 == None : return head1

    next1 = head1.next
    next2 = head2.next

    head1.next = head2
    head2.next = zipperlist(next1, next2)
    return head1


print(zipperlist(a,e))



# def zipperlist(head1, head2):
#     tail = head1
#     cur1 = head1.next
#     cur2 = head2
#     count = 0

#     while cur1 != None and cur2 != None:
#         if count%2 == 0 :
#             tail.next = cur2
#             cur2 = cur2.next
#         else : 
#             tail.next = cur1
#             cur1 = cur1.next
#         tail = tail.next
#         count += 1

#     if cur1 !=None : tail.next = cur1
#     if cur2 !=None : tail.next = cur2

#     return head1

# print(zipperlist(a,e))

    


# def reverseRecurrsion(head, prev = None):
#     if head == None : return prev
#     next = head.next
#     head.next = prev
#     return reverseRecurrsion(next, head)

# print(reverseRecurrsion(a))
# def reverselist(head):
#     prev = None
#     cur = head
#     while cur != None:
#         next = cur.next
#         cur.next = prev
#         prev = cur
#         cur = next
        
#     return prev


# print(reverselist(a))
# def getNodeValueIterative(head, index):
#     if head == None: return None
#     if index == 0 : return head.val

#     return getNodeValueIterative(head.next, index-1)

# print(getNodeValueIterative(a,4))

# def getNodeValue(head, index):
#     cur = head
#     count = 0
#     while cur != None:
#         if count == index : return cur.val
#         count += 1
#         cur = cur.next

# print(getNodeValue(a,4))


# def LinkedListFindRecurrsion(head, target):
#     if head == None : return False
#     if head.val == target : return True
#     return LinkedListFindRecurrsion(head.next, target)

# print(LinkedListFindRecurrsion(a, 5))

# print(LinkedListFindRecurrsion(a, 25))
# def fildLinkedList(head, target):
#     cur = head
#     while cur != None:
#         if cur.val == target:
#             return True
#         cur = cur.next
#     return False

# print(fildLinkedList(a,5))
# print(fildLinkedList(a,15))

# def sumLinkedListRecurrsion(head):
#     if head == None:
#         return 0
#     return head.val + sumLinkedListRecurrsion(head.next)


# print(sumLinkedListRecurrsion(a))

# def sumLinkedList(head):
#     sum = 0
#     cur = head

#     while(cur != None):
#         sum += cur.val
#         cur = cur.next 

#     return sum

# print(sumLinkedList(a))
# def linkedListRecurrsion(head):
#     values = []
#     fillvalues(head, values)
#     return values

# def fillvalues(head, values):
#     if head == None: return
#     values.append(head.val)
#     fillvalues(head.next,values)

# print(linkedListRecurrsion(a))

# def linkedListValues(head):
#     values = []
#     cur = head
#     while cur != None:
#         values.append(cur.val)
#         cur = cur.next
#     return values

# print(linkedListValues(a))

# def printLinkedList(head):
#     if head == None: return
#     print(head.val)
#     printLinkedList(head.next)


# printLinkedList(a)

# def printLinkedList(head):
#     current = head
#     while current != None:
#         print(current.val)
#         current = current.next
# printLinkedList(a)
# print("++++++++++++++++")
# printLinkedList(e)

