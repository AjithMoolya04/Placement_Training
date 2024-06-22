def binary_search_recursion(arr,target,left,right):
    if left>right:
        return -1
    mid=(left+right)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]<target:
        return binary_search_recursion(arr,target,mid+1,right)
    else:
        return binary_search_recursion(arr,target,left,mid-1)
    
    
arr=[1,2,3,4,5,6,7,8,9]
target=3
l=0
r=len(arr)-1
result=binary_search_recursion(arr,target,l,r)

if result!=-1:
    print("Element found at index",result) 
else:
    print("Element not found")  