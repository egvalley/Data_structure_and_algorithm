def merge(li,low,mid,high):
    ltmp=[]
    i=low
    j=mid+1
    while i<=mid and j<=high:
        if li[i]<li[j]:
            ltmp.append(li[i])
            i +=1
        else:
            ltmp.append(li[j])
            j+=1
    while i<=mid:
        ltmp.append(li[i])
        i+=1
    while j<=high:
        ltmp.append(li[j])
        j+=1
    li[low:high+1]=ltmp


def merge_sort(li,low,high):
    if low < high:
        mid=(low+high)//2
        merge_sort(li,low,mid)
        merge_sort(li,mid+1,high)
        merge(li,low,mid,high)


li=list(range(10))
import random
random.shuffle(li)
merge_sort(li,0,len(li)-1)
print(li)