import sys

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.color = 1            # 1-> Red / 0 -> Black

class RedBlacktree:
    def __init__(self):
        self.TNULL = Node(None)
        self.TNULL.color = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL

    def insert(self, value):
        node = Node(value)
        node.color = 1
        node.left = self.TNULL
        node.right = self.TNULL
        node.value = value
        node.parent = None

        y = None
        x = self.root

        while x!= self.TNULL:
            y = x
            if node.value < x.value:
                x = x.left
            else:
                x = x.right
        
        node.parent = y

        if y == None:
            self.root = node
        elif node.value < y.value:
            y.left = node
        else:
            y.right = node

        if node.parent == None:
            node.color = 0
            return
        
        if node.parent.parent == None:
            return
        self.fix_insert(node)

    def fix_insert(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.right_rotate(k.parent.parent)
            
            if k == self.root:
                break
        self.root.color = 0

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    def print_helper(self, node, intent, last):
        if node != self.TNULL:
            sys.stdout.write(intent)
            if last:
                sys.stdout.write("R----")
                intent += "     "
            else:
                sys.stdout.write("L----")
                intent+= "|    "
            
            s_color = "RED" if node.color == 1 else "BLACK"
            print(str(node.value) + "(" + s_color + ")")
            self.print_helper(node.left, intent, False)
            self.print_helper(node.right, intent, True)

    def print_tree(self):
        self.print_helper(self.root,"", True )

    def enable_delete(self,u,v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def delete_helper(self, node, value):
        z = self.TNULL
        while node != self.TNULL:
            if node.value == value:
                z = node

            if node.value <= value:
                node = node.right
            else:
                node = node.left

        if z == self.TNULL:
            print("Value not found in the tree")
            return
        
        y = z
        y_original_color = y.color

        if z.left == self.TNULL:
            x = z.right
            self.enable_delete(z,z.right)
        elif z.right == self.TNULL:
            x = z.left
            self.enable_delete(z,z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.enable_delete(y, y.right)
                y.right = z.right
                y.right.parent = y
            
            self.enable_delete(z,y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 0:
            self.delete_fix(x)

    def delete_fix(self,x):
        while x!=self.root and x.color == 0:
            if x == x.parent.left:
                s = x.parent.right
                # sibling is red
                if s.color == 1:
                    s.color = 0
                    s.parent.color = 1
                    self.left_rotate(x.parent)
                    s = x.parent.right

                # both children are black            
                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent

                else:
                    if s.right.color == 0:
                        s.left.color = 0
                        s.color = 1
                        self.right_rotate(s)
                        s = x.parent.right
                    
                    s.color = x.parent.color
                    x.parent.color = 0
                    s.right.color = 0
                    self.left_rotate(x.parent)
                    x = self.root

            else:
                s = x.parent.left
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.right_rotate(x.parent)
                    s = x.parent.left

                if s.right.color == 0 and s.left.color == 0:
                    s.color = 1
                    x = x.parent
                
                else:
                    if s.left.color == 0:
                        s.right.color == 0
                        s.color = 1
                        self.left_rotate(s)
                        s = x.parent.left

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.colr = 0
                    self.right_rotate(x.parent)
                    x = self.root
        
        x.color = 0

    def minimum(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node

    def delete_node(self, item):
        self.delete_helper(self.root, item)


bst = RedBlacktree()

l = [11,19,8,16,17,31,26,41,61,3,2,70]
for i in l:
    bst.insert(i)
bst.delete_node(70)
bst.delete_node(17)
bst.print_tree()
