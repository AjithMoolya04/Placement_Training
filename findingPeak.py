#find the peak element in the list of integer.peak elemnt is an element that is grater than or equal to it neighbor
def peak(num):
    if not num:
        return None
    
    left,right=0,len(num)-1
    while left<right:
        mid=left+(right-left)//2
        if num[mid]<num[mid+1]:
            left=mid+1
            
        else:
            right=mid
            
    return left
    
listt=[1,2,1,3,5,6,4]
print('peak element index',peak(listt))