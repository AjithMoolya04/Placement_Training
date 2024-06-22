# given an array of n number & another number x,the task is to check weather or not there exist 2 element in the array,whos exast sum is x

a=[1,1,2,4,8,-2]
x=2
def in_sum(a,x):
    pair=[]
    for i in range(0,len(a)):
        for j in range(0,len(a)):
            if a[i]+a[j]==x and i!=j:
                pair.append([a[i],a[j]])
    return pair
print(in_sum(a,x))


#now the better timecomplexity

a=[1,-2,1,0,2]
x=0

a.sort()
print(a)

def pair_sum(a,x):
    l=0
    r=len(a)-1
    pair=[]
    while(l<r):
        if a[l]+a[r]==x:
            pair.append([a[l],a[r]])
            return True
        elif a[l]+a[r]>x:
            r=r-1
        elif a[l]+a[r]<x:
            l=l+1
    return False


print(pair_sum(a,x))