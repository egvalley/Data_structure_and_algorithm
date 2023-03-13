from collections import deque

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


def print_path(path):
    cor_path=path[-1]
    ture_path=[]
    while cor_path[2] != -1:
        ture_path.append(cor_path[0:2])
        cor_path=path[cor_path[2]]
    ture_path.append(path[0][0:2])
    ture_path.reverse()
    print(ture_path)


def maze_queue(x1,y1,x2,y2):
    queue=deque()
    path=[]
    queue.append((x1,y1,-1))
    while len(queue)>0:
        curNode=queue.popleft()
        path.append(curNode)
        if curNode[0]== x2 and curNode[1]==y2:
            print_path(path)
            return True
        for dir in dirs:
            nextNode=dir(curNode[0],curNode[1])
            if maze[nextNode[0]][nextNode[1]]==0:
                queue.append((nextNode[0],nextNode[1],len(path)-1))
                maze[nextNode[0]][nextNode[1]]=2
    else:
        print('NONE')
        return False


maze_queue(1,1,8,8)