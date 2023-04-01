inorder = [4,2,5,1,6,3,7]
levelorder = [1,2,3,4,5,6,7]

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class binary_tree:
    def inorder(self, root):
        if root is None:
            return 
        self.inorder(root.left)
        print(root.value, end = " ")
        self.inorder(root.right)
    
    def construct(self, inorder, start, end, d):
        
        if start > end:
            return None
        index = start
        for j in range(start+1, end+1):
            if d.get(inorder[j]) < d.get(inorder[index]):
                index = j

        root = Node(inorder[index])
        root.left = self.construct(inorder, start, index-1,d)
        root.right = self.construct(inorder, index+1, end,d)

        return root

    def constructTree(self, inorder, levelorder):
        d = {}
        for i,e in enumerate(levelorder):
            d[e] = i
        print(d)

        return self.construct(inorder, 0, len(inorder)-1, d)


tree = binary_tree()
root = tree.constructTree(inorder, levelorder)
print(root)

tree.inorder(root)