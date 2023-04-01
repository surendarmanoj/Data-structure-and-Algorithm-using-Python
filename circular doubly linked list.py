class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class circular_doubly_linked_list:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
            self.head.prev = self.head
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        cur = self.head
        new_node.next = self.head

        if not self.head:
            new_node.next = new_node
            new_node.prev = new_node
        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
        self.head = new_node


    def remove_key_node(self, key):
        if self.head.data == key:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            next = self.head.next
            next.prev = cur.next
            cur.next = next
            self.head = next
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur.data == key:
                    prev.next = cur.next
                    cur.next.prev = prev

    def __len__(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
            if cur == self.head:
                break
        return count


    def split_list(self):
        size = len(self)
        if size == 0:
            return None
        if size == 1:
            return self.head
        
        mid = size // 2
        count = 0
        prev = None
        cur = self.head
        while cur and count < mid:
            count += 1
            prev = cur
            cur = cur.next
        prev.next = self.head
        self.head.prev = prev

        split_cdll = circular_doubly_linked_list()
        while cur.next != self.head:
            split_cdll.append(cur.data)
            cur = cur.next
        split_cdll.append(cur.data)
        print("\n")
        self.print_list()
        print("\n")
        split_cdll.print_list()





    def print_list(self):
        cur = self.head
        while self.head: 
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break


cdll = circular_doubly_linked_list()
cdll.append("A")
cdll.append("B")
cdll.append("C")
cdll.append("D")
cdll.prepend("E")
cdll.prepend("F")
# cdll.remove_key_node("A")
cdll.print_list()
cdll.split_list()