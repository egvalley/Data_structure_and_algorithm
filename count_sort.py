def count_sort(li,maxnum):
    count=[0 for _ in range(maxnum+1)]
    for val in li:
        count[val]+=1
    li.clear()
    for ind, val in enumerate(count):
        for i in range(val):
            li.append(ind)

import random

li=[random.randint(0,100) for _ in range(100)]

count_sort(li,100)
print(li)
