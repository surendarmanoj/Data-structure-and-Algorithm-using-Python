inorder = [9,5,1,7,2,12,8,4,3,11]
postorder = [9,1,2,12,7,5,3,11,4,8]

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
        print(root.value, end=" ")
        self.inorder(root.right)

    def postorder(self, root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.value, end=" ")


    def construct(self, start, end, postorder, pIndex, d ):
        if start > end:
            return None, pIndex
        
        root = Node(postorder[pIndex])
        pIndex -= 1
        index = d[root.value]

        root.right, pIndex = self.construct(index+1, end, postorder, pIndex, d)
        root.left, pIndex = self.construct(start, index-1, postorder, pIndex, d)
        
        return root, pIndex
    
    def constructTree(self, inorder, postorder):
        d = {}
        for i,e in enumerate(inorder):
            d[e] = i
        print(d)
        n = len(inorder)
        pIndex = n-1

        return self.construct(0, n-1, postorder, pIndex, d)[0]  


tree = binary_tree()
root  =tree.constructTree(inorder, postorder)    
print(root)
tree.inorder(root)
print("\n")
tree.postorder(root)