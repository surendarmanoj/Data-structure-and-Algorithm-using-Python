inorder = [4,2,1,7,5,8,3,6]
preorder = [1,2,4,3,5,7,8,6]

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class Binary_tree:
    def inorderTraversal(self, root):
        if root is None:
            return
        self.inorderTraversal(root.left)
        print(root.value, end = " ")
        self.inorderTraversal(root.right)

    def preordertraversal(self, root):
        if root is None:
            return
        print(root.value, end = " ")
        self.preordertraversal(root.left)
        self.preordertraversal(root.right)
    
    def construct(self, start, end, preorder, pIndex, d):
        if start > end:
            return None, pIndex
        
        root = Node(preorder[pIndex])
        pIndex += 1

        index = d[root.value]

        root.left, pIndex = self.construct(start, index-1, preorder,pIndex, d)
        root.right, pIndex = self.construct(index+1,end, preorder,pIndex, d)

        return root, pIndex


    
    def constructTree(self, inorder, preorder):
        # hashmap creation
        d = {}
        for i, e in enumerate(inorder):
            d[e] = i
        print(d)
        # root at 0th index of preorder
        pIndex = 0

        return self.construct(0, len(inorder)-1, preorder, pIndex, d)[0]
    

tree = Binary_tree()
root = tree.constructTree(inorder, preorder)
print(root)

tree.inorderTraversal(root)
print("\n")
tree.preordertraversal(root)