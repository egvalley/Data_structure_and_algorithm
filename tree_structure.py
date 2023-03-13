class Node:
    def __init__(self,name,Type="dir"):
        self.name=name
        self.Type=Type
        self.children=[]
        self.parent=None
    def __repr__(self):
        return self.name

class TreeSystem:
    def __init__(self):
        self.root=Node("root/")
        self.nownode=self.root

    def ls(self):
        return self.nownode.children

    def mkdir(self,name):
        if name[-1] !="/":
            name +="/"
        child=Node(name)
        child.parent=self.nownode
        self.nownode.children.append(child)

    def cd(self,name):
        if name[-1] !="/":
            name +="/"

        if name=="../":
            self.nownode = self.nownode.parent
            return

        for child in self.nownode.children:
            if name==child.name:
                self.nownode=child
                break
        else:
            raise ValueError("not existed")



tree=TreeSystem()
tree.mkdir("user")
tree.mkdir("disk")
tree.mkdir("file")
print(tree.ls())
tree.cd("file")
tree.mkdir("file_son1")
print(tree.ls())
tree.cd("../")
print(tree.ls())

