def binarysearch( arr,key):
    l=0
    h=len(arr)-1
    
    while(l<=h):
        mid=l+(h-l)//2
        if arr[mid]==key:
            return ("eleemnty is found at position",mid)
            break
        elif key>arr[mid]:
            l=mid+1
        else:
            h=mid-1
print(binarysearch([11,12,13,14,15],14))
