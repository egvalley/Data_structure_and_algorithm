import random


def select_sort(li):

    for i in range(len(li)-1):
        loc_min=i
        for j in range(i,len(li)):
            if li[loc_min]>li[j]:
                loc_min=j
        li[i],li[loc_min] = li[loc_min],li[i]
        print(li)

li=[6,23,56,1,5,9,65]