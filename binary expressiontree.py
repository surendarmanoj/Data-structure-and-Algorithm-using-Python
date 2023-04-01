p_fix = "ab-cd*e*-"

class Node(object):
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def isOperator(c):
    if (c == '+' or c =='-' or c == '*' or c == '/' or c == '^'):
        return True
    else:
        return False
def inorder_traversal(start):
    "Left => Root => Right"
    if start:
        inorder_traversal(start.left)
        print(start.value, end = " ")
        inorder_traversal(start.right)

def constructTree(postfix):
    stack = []
    for char in postfix:
        t = Node(char)
        if isOperator(char):
            t1 = stack.pop()
            t2 = stack.pop()
            t.right = t1
            t.left = t2
        stack.append(t)
    t = stack.pop()
    return t

op = constructTree(p_fix)
inorder_traversal(op)