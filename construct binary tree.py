inorder = [4, 2, 1, 7, 5, 8, 3, 6]
preorder = [1, 2, 4, 3, 5, 7, 8, 6]


# A class to store a binary tree node
class Node:
    # Constructor
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
class Binary_tree:
    # Recursive function to perform inorder traversal on a given binary tree
    def inorderTraversal(self,root):
        if root is None:
            return
    
        self.inorderTraversal(root.left)
        print(root.data, end=' ')
        self.inorderTraversal(root.right)
    
    
    # Recursive function to perform postorder traversal on a given binary tree
    def preorderTraversal(self,root):
        if root is None:
            return
    
        print(root.data, end=' ')
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)
    
    
    # Recursive function to construct a binary tree from a given
    # inorder and preorder sequence
    def construct(self,start, end, preorder, pIndex, d):
    
        # base case
        if start > end:
            return None, pIndex
    
        # The next element in `preorder[]` will be the root node of subtree
        # formed by sequence represented by `inorder[start, end]`
        root = Node(preorder[pIndex])
        pIndex = pIndex + 1
    
        # get the index of the root node in inorder to determine the
        # left and right subtree boundary
        index = d[root.data]
    
        # recursively construct the left subtree
        root.left, pIndex = self.construct(start, index - 1, preorder, pIndex, d)
    
        # recursively construct the right subtree
        root.right, pIndex = self.construct(index + 1, end, preorder, pIndex, d)
    
        # return current node
        return root, pIndex
    
    
    # Construct a binary tree from inorder and preorder traversals.
    # This function assumes that the input is valid
    # i.e., given inorder and preorder sequence forms a binary tree
    def constructTree(self,inorder, preorder):
    
        # create a dictionary to efficiently find the index of any element in
        # a given inorder sequence
        d = {}
        for i, e in enumerate(inorder):
            d[e] = i
    
        # `pIndex` stores the index of the next unprocessed node in a preorder sequence;
        # start with the root node (present at 0th index)
        pIndex = 0
    
        return self.construct(0, len(inorder) - 1, preorder, pIndex, d)[0]
    
    
    
    
tree = Binary_tree()    
root = tree.constructTree(inorder, preorder)

# traverse the constructed tree
print('The inorder traversal is ', end='')
tree.inorderTraversal(root)

print('\nThe preorder traversal is ', end='')
tree.preorderTraversal(root)