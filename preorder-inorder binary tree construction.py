preorder = [1,2,4,5,3,6,8,9,7]
postorder = [4,5,2,8,9,6,7,3,1]


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class binary_tree:
    def Inorder(self, root):
        if root is None:
            return
        self.Inorder(root.left)
        print(root.value, end = " ")
        self.Inorder(root.right)

    def construct(self, preorder, pIndex, start, end, d):
        root = Node(preorder[pIndex])
        pIndex += 1

        if pIndex == len(preorder):
            return root, pIndex

        index = d.get(preorder[pIndex])

        if start <= index and index+1 <= end - 1:
            root.left, pIndex = self.construct(preorder, pIndex, start,index,d)
            root.right, pIndex = self.construct(preorder, pIndex, index+1,end-1,d)

        return root, pIndex

    def constructTree(self, preorder, postorder):
        if not preorder:
            return
        
        d = {}
        for i,e in enumerate(postorder):
            d[e] = i
        print(d)

        pIndex = 0
        start = 0
        end = len(preorder) - 1
        return self.construct(preorder, pIndex, start, end,d)[0]
    
tree = binary_tree()
root = tree.constructTree(preorder, postorder)
print(root)

print("\n")
tree.Inorder(root)