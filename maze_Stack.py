maze=[
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,0,0,1,1,0,0,1],
    [1,0,0,0,0,0,1,1,1,1],
    [1,0,1,1,1,0,0,0,0,1],
    [1,0,0,0,1,0,0,0,0,1],
    [1,0,1,0,0,0,1,0,0,1],
    [1,0,1,1,1,0,1,1,0,1],
    [1,1,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
]

dirs=[
    lambda x,y:(x+1,y),
    lambda x,y:(x-1,y),
    lambda x,y:(x,y-1),
    lambda x,y:(x,y+1)
]

class Stack():
   def __init__(self):
       self.stack=[]

   def push(self,element):
       self.stack.append(element)

   def pop(self):
       return self.stack.pop()

   def get_top(self):
       if len(self.stack)>0:
           return self.stack[-1]
       else:
           return None

   def is_empty(self):
       return len(self.stack)==0

def maze_s(x1,y1,x2,y2):
    ST=Stack()
    ST.push((x1,y1))
    while len(ST.stack)>0:
        curNode=ST.get_top()
        if curNode[0]==x2 and curNode[1]==y2:
            print(ST.stack)
            return True
        else:
            for dir in dirs:
                nextNode =dir(curNode[0],curNode[1])
                if maze[nextNode[0]][nextNode[1]] == 0:
                    maze[nextNode[0]][nextNode[1]]=2
                    ST.push(nextNode)
                    break
            else:
                ST.pop()
    else:
        return False


print(maze_s(1,1,8,8))