n=int(input())
arr=[]
print("enter the array elements")
for i in range(0,n-k+1):
    arr.append(input())
k=int(input())
count=[]
result=[]
for i in range(n-k+1):
    window=arr[i:i+k]
    count=len(set(window))
    result.append(count)
print(result)

    
