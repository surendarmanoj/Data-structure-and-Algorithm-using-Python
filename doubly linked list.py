class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        if self.head == None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None

    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def add_after_node(self, data, key):
        cur = self.head
        while cur:      
            if cur.next is None and cur.data == key:
                self.append(data)
                return 
            elif cur.data == key:
                new_node = Node(data)
                next = cur.next
                cur.next = new_node
                new_node.next = next
                new_node.prv = cur
                next.prev = new_node
            cur = cur.next

    def append_before_node(self, data, key):
        cur = self.head
        while cur:      
            if cur.next is None and cur.data == key:
                self.prepend(data)
                return 
            elif cur.data == key:
                new_node = Node(data)
                prev = cur.prev
                prev.next = new_node
                cur.prev = new_node
                new_node.next = cur
                new_node.prev = prev
            cur = cur.next


    def delete(self, key):
        cur = self.head
        while cur:
            if cur.data == key and cur== self.head:
                # deleting the head and head is only element
                if cur.next is None:
                    cur = None
                    self.head = None
                    return
                #deleting a head node not only element
                else:
                    next = cur.next
                    cur.next = None
                    next.prev = None
                    cur = None
                    self.head = next
                    return

            elif cur.data == key:
                # delete a node from middle
                if cur.next:
                    next = cur.next
                    prev = cur.prev
                    prev.next = next
                    next.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return
                
                # deleting the tail element
                else:
                    prev = cur.prev
                    prev.next = None
                    cur.prev = None
                    cur = None
                    return
            cur = cur.next
    
    
    def reverse(self):
        temp = None
        cur = self.head
        while cur:
            temp = cur.prev
            cur.prev = cur.next
            cur.next = temp
            cur = cur.prev
            if temp:
                self.head = temp.prev
        






dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.add_after_node(8,4)
dll.append_before_node(7,3)
dll.print_list()
dll.reverse()
print("____________________")
dll.print_list()