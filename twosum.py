def summ(arry,target):
    for i in range(0,len(arry)):
        for j in  range(1,len(arry)):
            if arry[i]+arry[j]==target:
                return i,j
arry=[1,2,4,5,6,7,8]
target=9
print(summ(arry,target))

