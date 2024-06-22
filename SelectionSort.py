#selection sort
def selection_sort(arr):
    n=len(arr)
    for i in range(0,n-1):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
arr=[60,20,30,40,50,10,80,90,70]
selection_sort(arr)
print("sorted array:",arr)