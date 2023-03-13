def radix_sort(li):
    max_num=max(li)
    it=0
    while 10**it <= max_num:
        buc=[[] for _ in range(10)]
        for val in li:
            buc_num= (val//(10**it))%10
            buc[buc_num].append(val)
        li.clear()
        for array in buc:
            li.extend(array)
        it +=1

import random
li=list(range(10000))
random.shuffle(li)
radix_sort(li)
print(li)