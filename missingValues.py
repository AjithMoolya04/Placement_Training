#even an array of size n-1 such that it only contains distinct integers in the range of 1 to n.find thr missing element
#input n=10
#array=[6,1,5,8,2,3,4,7,10]   

def find_missing_ele(arr,n):
    total_sum=n*(n+1)//2
    array_sum=sum(arr)
    return total_sum-array_sum

n=10
arr=[6,1,5,8,2,3,4,7,10]
print(find_missing_ele(arr,n))