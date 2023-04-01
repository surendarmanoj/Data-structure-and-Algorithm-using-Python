arr = [15,10,20,8,12,16]

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class binary_search_tree:
    def inorder(self,root):
        if root == None:
            return
        self.inorder(root.left)
        print(root.value, end = " ")
        self.inorder(root.right)

    def insert(self, root, value):
        if root is None:
            return Node(value)
        
        if value < root.value:
            root.left = self.insert(root.left, value)
        elif value > root.value:
            root.right = self.insert(root.right, value)
        else:
            print("Value already in the tree")

        return root
    
    def delete(self, root, value):
        parent = None
        cur = root
        while cur and cur.value != value:
            parent = cur

            if value < cur.value:
                cur = cur.left
            else:
                cur = cur.right

        if cur == None:
            return root
        
        #case 1 - No child
        if cur.left == None and cur.right == None:
            if cur != root:
                if parent.left == cur:
                    parent.left = None
                else:
                    parent.right = None
            else:
                root = None
        
        #case 2: one left child
        elif cur.left!= None and cur.right == None:
            child = cur.left
            if cur != root:
                if cur == parent.left:
                    parent.left = child
            else:
                root = child
        #case 3: One Right Child
        elif cur.left== None and cur.right != None:
            child = cur.right
            if cur != root:
                if cur == parent.right:
                    parent.right = child
            else:
                root = child
        #case4 : 2 children
        elif cur.left and cur.right:
            next_val = self.getMin(cur.right)

            val = next_val.value

            self.delete(root, next_val.value)
            cur.value = val
        return root
        

    def getMin(self, cur):
        while cur.left:
            cur = cur.left
        return cur


            

tree = binary_search_tree()
root = None
for i in arr:
    root = tree.insert(root, i)

tree.inorder(root)
root = tree.delete(root, 16)
print("\n")
tree.inorder(root)