preorder = [15,10,8,12,20,16,25]
postorder = [8,12,10,16,25,20,15]


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BST:
    def inorder(self, root):
        if root == None:
            return
        self.inorder(root.left)
        print(root.value, end = " ")
        self.inorder(root.right)


    def constructTree_pre(self, preorder, start, end):
        if start > end:
            return None
        
        node = Node(preorder[start])
        i = start
        while i<= end:
            if preorder[i] > node.value:
                break
            i+=1
        node.left = self.constructTree_pre(preorder, start+1,i-1 )
        node.right = self.constructTree_pre(preorder,i, end)
        return node
    
    def constructBST_post(self, postorder, start, end):
        if start > end:
            return None
        
        node = Node(postorder[end])
        i = end
        while i >= start:
            if postorder[i] < node.value:
                break
            i -= 1
        
        node.left = self.constructBST_post(postorder, start, i)
        node.right = self.constructBST_post(postorder,i+1, end - 1 )
        return node


tree = BST()
root = tree.constructTree_pre(preorder,0, len(preorder)-1)
tree.inorder(root)
print("\n")
root1 = tree.constructBST_post(postorder,0, len(postorder)-1)
tree.inorder(root1)
