from random import randint

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class binary_tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
            print(self.root.value)
        else:
            self.insert_help(value, self.root)

    def insert_help(self, value, cur_node):

        if value < cur_node.value:
            if cur_node.left == None:
                cur_node.left = Node(value)
            else:
                self.insert_help(value, cur_node.left)

        elif value > cur_node.value:
            if cur_node.right == None:
                cur_node.right = Node(value)
            else:
                self.insert_help(value, cur_node.right)
    
    def print_tree(self):
        if self.root != None:
            self.inorder(self.root)

    def inorder(self, cur_node):
        if cur_node!= None:
            self.inorder(cur_node.left)
            print(cur_node.value, end = ",")
            self.inorder(cur_node.right)
    
    def search(self, value):
        if self.root == None:
            return False
        else:
            return self.search_helper(value, self.root)

    def search_helper(self, value, cur_node):
        if value == cur_node.value:
            return True
        elif value < cur_node.value and cur_node.left != None:
            return self.search_helper(value, cur_node.left)
        elif value > cur_node.value and cur_node.right != None:
            return self.search_helper(value, cur_node.right)
        else:
            return False
  

    
def fill_tree(tree, num = 100, maxim=1000):
    for k in range(num):
        cur_ele = randint(0, maxim)
        tree.insert(cur_ele)
    return tree

tree = binary_tree()
tree = fill_tree(tree)
# tree.insert(10)
# tree.insert(2)
# tree.insert(6)
# tree.insert(4)
# tree.insert(14)
# tree.insert(20)
# tree.insert(0)
# tree.insert(40)


tree.print_tree()
print(tree.search(30))
