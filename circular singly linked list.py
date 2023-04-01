class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class circular_singly_linked_list:

    def __init__(self):
        self.head = None

    

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head

    def prepend(self, data):
            new_node = Node(data)
            cur = self.head
            new_node.next = self.head

            if not self.head:
                new_node.next = new_node

            else:
                while cur.next != self.head:
                    cur = cur.next
                cur.next = new_node
            self.head = new_node


    def remove_key_node(self, key):
        if self.head.data == key:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = self.head.next
            self.head = self.head.next

        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
            
                if cur.data == key:
                    prev.next = cur.next
                    cur = cur.next

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
        mid = size //2
        count = 0
        prev = None
        cur = self.head
        while cur and count < mid:
            count += 1
            prev = cur
            cur = cur.next
        prev.next = self.head
        split_csll = circular_singly_linked_list()
        while cur.next != self.head:
            split_csll.append(cur.data)
            cur = cur.next
        split_csll.append(cur.data)
        print("\n")
        self.print_list()
        print("\n")
        split_csll.print_list()



    def print_list(self):
        cur = self.head
        while self.head:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break

    def is_circular_linked_list(self, input_list):
        cur = input_list.head

        while cur.next:
            cur = cur.next
            if cur.next == input_list.head:
                return True
        return False
        
csll = circular_singly_linked_list()

csll.append("A")
csll.append("B")
csll.append("C")
csll.append("D")
csll.prepend("E")
csll.prepend("F")
# csll.remove_key_node("B")
csll.print_list()
print(len(csll))
csll.split_list()

print(csll.is_circular_linked_list(csll))