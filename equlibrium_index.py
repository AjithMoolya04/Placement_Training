# an equlibrium index is an index such that the sum of element of lower indices is equal to sum of element higher indecyec.exaple a=[-7,1,5,2,-4,3,0]
#output is 3    else return 1 if no such points exists 

def equlibrium(arr):
    n=len(arr)
    for i in range(n):
        lsum=sum(arr[:i])
        rsum=sum(arr[i+1:])
        if lsum==rsum:
            return i
    return -1

arr=[-7,1,5,2,-4,3,0]
print(equlibrium(arr))