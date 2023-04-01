class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def is_empty(self):
        return len(self.items) == 0
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        
    def peek(self):
        if not self.is_empty():
            return self.items[-1].value
        
    def size(self):
        return len(self.items)
    
    def __len__(self):
        return self.size()
        
    


class Queue(object):
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.insert(0,item)

    def is_empty(self):
        return len(self.items) == 0
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        
    def peek(self):
        if not self.is_empty():
            return self.items[-1].value
        
    def size(self):
        return len(self.items)
    
    def __len__(self):
        return self.size()

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_traversal(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_traversal(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_traversal(tree.root, "")
        elif traversal_type == "levelorder":
            return self.level_order_traversal(tree.root, "")
        elif traversal_type == "reverselevelorder":
            return self.reverse_level_order_traversal(tree.root, "")
        elif traversal_type == "height":
            return self.height(tree.root)
        elif traversal_type == "size":
            return self.size_ot_tree()
        elif traversal_type == "size_r":
            return self.size_recurrsion(tree.root)
        else:
            return "Traversal type not defined"


    def preorder_traversal(self, start, traversal):
        "Root => Left => Right"
        if start:
            traversal += (str(start.value) + " - ")
            traversal = self.preorder_traversal(start.left, traversal)
            traversal = self.preorder_traversal(start.right, traversal)
        return traversal

    def inorder_traversal(self, start, traversal):
        "Left => Root => Right"
        if start:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal += (str(start.value) + " - ")
            traversal = self.preorder_traversal(start.right, traversal)
        return traversal

    def postorder_traversal(self, start, traversal):
        "Left => Right => Root"
        if start:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal = self.preorder_traversal(start.right, traversal)
            traversal += (str(start.value) + " - ")
        return traversal

   
    def level_order_traversal(self, start, traversal):
        if start is None:
            return
        
        queue = Queue()
        queue.enqueue(start)

        while len(queue) > 0 :
            traversal += str(queue.peek()) + " - "
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return traversal

    def reverse_level_order_traversal(self, start, traversal):
        if start is None:
            return
        
        queue = Queue()
        stack = Stack()

        queue.enqueue(start)

        while len(queue) > 0:
            node = queue.dequeue()
            stack.push(node)

            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)
        
        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.value) + " - "
        return traversal
    
    def height(self, node):
        if node is None:
            return -1
        
        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return max(left_height, right_height) + 1
    
    def size_ot_tree(self):
        if self.root is None:
            return 0
        
        stack = Stack()
        stack.push(self.root)
        size = 1
        while stack:
            node = stack.pop()
            if node.left:
                size += 1
                stack.push(node.left)
            if node.right:
                size += 1
                stack.push(node.right)

        return size
    
    def size_recurrsion(self, node):
        if node is None:
            return 0
        return 1+ self.size_recurrsion(node.left) + self.size_recurrsion(node.right)
    


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)
tree.root.right.right.left = Node(9)

print(tree.print_tree("preorder"))
print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))
print(tree.print_tree("levelorder"))
print(tree.print_tree("reverselevelorder"))
print(tree.print_tree("height"))
print(tree.print_tree("size"))
print(tree.print_tree("size_r"))
