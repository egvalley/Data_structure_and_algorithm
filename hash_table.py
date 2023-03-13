class LinkList:
    class Node:
        def __init__(self,item=None):
            self.item=item
            self.next=None

    class LinkListIterator:
        def __init__(self,node):
            self.node=node
        def __next__(self):
            if self.node:
                cur_node=self.node
                self.node=cur_node.next
                return cur_node.item
            else:
                raise StopIteration
        #def __iter__(self):
        #    return self

    def __init__(self,iterable=None):
        self.head=None
        self.tail=None
        if iterable:
            self.extend(iterable)

    def append(self,obj):
        s= LinkList.Node(obj)
        if not self.head:
            self.head=s
            self.tail=s
        else:
            self.tail.next=s
            self.tail=s

    def extend(self,iterable):
        for obj in iterable:
            self.append(obj)

    def find(self,obj):
        for n in self:
            if n==obj:
                return True
        else:
            return False

    def __iter__(self):
        return self.LinkListIterator(self.head)

    def __repr__(self):
        return "<<"+".".join(map(str,self))+">>"



class Hash_table:
    def __init__(self,size):
        self.size=size
        self.Table=[LinkList() for _ in range(size)]

    def h_function(self,para_x):
        return para_x % self.size

    def insert(self,obj):
        LinkList_num=self.h_function(obj)
        if self.find(obj):
            print("duplicated inserting")
        else:
            self.Table[LinkList_num].append(obj)

    def find(self,obj):
        LinkList_num=self.h_function(obj)
        return self.Table[LinkList_num].find(obj)


ht=Hash_table(20)
ht.insert(2)
ht.insert(3)
ht.insert(23)
print(",".join(map(str,ht.Table)))
