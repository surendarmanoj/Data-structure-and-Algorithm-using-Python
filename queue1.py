class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    #enqueue
    def Enqueue(self, data):
        if self.tail is None:
            self.head = self.tail = Node(data)
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
        # return self.data

    #dequeue
    def dequeue(self):
        if self.head is None:
            return("Queue is empty")
        else:
            dele = self.head.data
            self.head = self.head.next
            return dele
    #check if empty
    def Isempty(self):
        return self.head is None

    #sizeof
    def sizeof(self):
        count = 0
        cur = self.head
        while(cur):
            count += 1
            cur = cur.next
        return count

    #peek
    def peek(self):
        return self.head.data

    def last(self):
        return self.tail.data

q = Queue()


print("+++++++++++++++++")
print(q.Enqueue(1))
print(q.Enqueue(2))
print(q.Enqueue(3))
print(q.peek())
print(q.last())
print("==================")
print(q.deueue())
print("++++++++++++++")
print(q.peek())
print(q.last())