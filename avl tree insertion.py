class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.height = 1


class AVL_Tree:
    def insert(self, root, value):
        if not root:
            return Node(value)
        elif value < root.value:
            root.left = self.insert(root.left, value)
        elif value > root.value:
            root.right = self.insert(root.right, value)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and value < root.left.value:
            return self.right_rotate(root)
        if balance < -1 and value > root.right.value:
            return self.left_rotate(root)
        if balance > 1 and value > root.left.value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and value < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        return root

    def delete(self, root, value):
        if not root:
            return root
        
        elif value < root.value:
            root.left = self.delete(root.left, value)
        
        elif value > root.value:
            root.right = self.delete(root.right, value)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            
            temp = self.get_min_value_node(root.right)
            root.value = temp.value
            root.right = self.delete(root.right, temp.value)
        
        if root is None:
            return root
        
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)
        
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)
        
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        return root

        

        

    def get_min_value_node(self, root):
        if root is None or root.left is None:
            return root
        return self.get_min_value_node(root.left)

    def left_rotate(self,z):
        y = z.right
        t = y.left

        y.left = z
        z.right = t

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        t = y.right

        y.right = z
        z.left = t

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def inorder_traversal(self, root):
        result = []
        if not root:
            return result
        result += self.inorder_traversal(root.left)
        result.append(root.value)
        result += self.inorder_traversal(root.right)
        return result
    

avl_tree = AVL_Tree()
root = None
root = avl_tree.insert(root, 14)
root = avl_tree.insert(root, 11)
root = avl_tree.insert(root, 19)
root = avl_tree.insert(root, 7)
root = avl_tree.insert(root, 12)
root = avl_tree.insert(root, 17)
root = avl_tree.insert(root, 53)
root = avl_tree.insert(root, 4)
root = avl_tree.insert(root, 8)
root = avl_tree.insert(root, 13)
root = avl_tree.insert(root, 16)
root = avl_tree.insert(root, 20)
root = avl_tree.insert(root, 60)
print(avl_tree.inorder_traversal(root))
root = avl_tree.delete(root,8)
print(avl_tree.inorder_traversal(root))
root = avl_tree.delete(root,7)
print(avl_tree.inorder_traversal(root))
root = avl_tree.delete(root,11)
print(avl_tree.inorder_traversal(root))
root = avl_tree.delete(root,14)
print(avl_tree.inorder_traversal(root))
root = avl_tree.delete(root,17)
print(avl_tree.inorder_traversal(root))