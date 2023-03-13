class Que_q:
    def __init__(self,size):
        self.queue_q=[0 for _ in range(size)]
        self.front=0
        self.rear=0
        self.size=size

    def push(self,element):
        if not self.is_fiiled():
            self.rear=(self.rear+1)%self.size
            self.queue_q[self.rear]=element
        else:
            raise IndexError('满了')

    def pop(self):
        if not self.is_empty():
            self.front=(self.front+1)%self.size
            return self.queue_q[self.front]
        else:
            raise IndexError('出错了')

    def is_empty(self):
        return self.front==self.rear

    def is_fiiled(self):
        return (self.rear+1)%self.size==self.front

q=Que_q(5)
for i in range(4):
    q.push(i)
print(q.queue_q)