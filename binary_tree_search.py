class Node:
    def __init__(self,data):
        self.data=data
        self.lchild=None
        self.rchild=None
        self.parent=None

class BTS:
    def __init__(self,li=None):
        self.root=None
        if li:
            for ele in li:
                self.insert(self.root,ele)

    def pre_order(self,root):
        if root:
            print(root.data,end=",")
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)

    def in_order(self,root):
        if root:
            self.in_order(root.lchild)
            print(root.data,end=",")
            self.in_order(root.rchild)

    def insert(self,node,val):
        if not self.root:
            node = Node(val)
            self.root=node
        else:
            if not node:
                node=Node(val)
            elif val<node.data:
                node.lchild=self.insert(node.lchild,val)
                node.lchild.parent=node
            elif val>node.data:
                node.rchild=self.insert(node.rchild,val)
                node.rchild.parent=node
        return node

    def insert_no_recu(self,val):
        node=self.root
        if not node:
            self.root=Node(val)
            return
        while True:
            if val<node.data:
                if not node.lchild:
                    node.lchild=Node(val)
                    node.lchild.parent=node
                    return
                else:
                    node=node.lchild
            elif val>node.data:

                if not node.rchild:
                    node.rchild=Node(val)
                    node.rchild.parent=node
                    return
                else:
                    node=node.rchild
            else:
                return

li=list(range(50))
import random
random.shuffle(li)
tree=BTS(li)
tree.pre_order(tree.root)
print("")
tree.in_order(tree.root)