def quicksort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[len(arr)//2]
    left=[x for x in arr if x<pivot]
    midle=[x for x in arr if x==pivot]
    right=[x for x in arr if x>pivot]
    return quicksort(left)+midle+quicksort(right)
arr=[12,11,13,5,6,7]
print("given aryy is :",arr)
print("sorted array;",quicksort(arr))

