import random

import sys
sys.setrecursionlimit(10000)

def quick_sort(li,left,right):
    if left < right:
        mid=part_sort(li,left,right)
        quick_sort(li,left,mid-1)
        quick_sort(li,mid+1,right)



def part_sort(li,left,right):
    tmp=li[left]
    while left < right:
        while li[right]>=tmp and left<right:
            right -=1
        li[left] = li[right]
        while li[left]<=tmp and left<right:
            left +=1
        li[right]=li[left]
    li[left] = tmp
    return left

li=list(range(10))
random.shuffle(li)
quick_sort(li,0,len(li)-1)
print(li)