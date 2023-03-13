def bucket_sort(li,n,maxnum):
    bucket=[[] for _ in range(n)]
    for val in li:
        i=min(val//(maxnum//n),n-1)
        bucket[i].append(val)
        for j in range(len(bucket[i])-1,0,-1):
            if bucket[i][j]<bucket[i][j-1]:
                bucket[i][j],bucket[i][j-1]=bucket[i][j-1],bucket[i][j]
            else:
                break
    sorted_li=[]
    for buc in bucket:
        sorted_li.extend(buc)
    return sorted_li

import random

li=[random.randint(0,100) for _ in range(20)]

sorted_li=bucket_sort(li,5,100)
print(sorted_li)