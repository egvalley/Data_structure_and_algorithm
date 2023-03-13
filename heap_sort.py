def sift(li,low,high):
    i=low
    j=2*i+1
    tmp=li[low]
    while j<=high:
        if j<high and li[j+1]>li[j]:
            j += 1
        if li[j]>tmp:
            li[i]=li[j]
            i=j
            j=2*i+1
        else:
            li[i]=tmp
            break
    else:
        li[i]=tmp

def heap_sort(li):
    for i in range((len(li)-2)//2,-1,-1):
        sift(li,i,len(li)-1)
    for j in range(len(li)-1,-1,-1):
        li[j],li[0]=li[0],li[j]
        sift(li,0,j-1)


li=list(range(50))
import random
random.shuffle(li)
heap_sort(li)
print(li)