def insertionsort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j=j-1
            arr[j+1]=key

arr=[60,20,30,40,50,10,80,90,70]
insertionsort(arr)


