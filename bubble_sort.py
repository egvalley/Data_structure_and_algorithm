def bubble_sort(li):
    for i in range(len(li)-1):
        for j in range(len(li)-1-i):
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
        print(li)

li=[6,23,56,1,5,9,65]
bubble_sort(li)
print(li)