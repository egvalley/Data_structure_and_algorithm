def shell_sort(li):
    gap=len(li)//2
    while gap>=1:
        for i in range(gap,len(li)):
            tmp=li[i]
            j = i-gap
            while li[j]>tmp and j>=0:
                li[j+gap]=li[j]
                j = j-gap
            li[j+gap]=tmp
        gap //=2


li=list(range(10))
import random
random.shuffle(li)
shell_sort(li)
print(li)
