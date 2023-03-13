import random


def func(li):

    for i in range(1,len(li)):
        tmp=li[i]
        j=i-1
        while j>=0 and li[j]<tmp:
            li[j+1]=li[j]
            j -= 1
        li[j+1]=tmp
        print(li)

li=list(range(10))
random.shuffle(li)
func(li)
print(li)