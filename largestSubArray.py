#find the largest sub array sum in the given list
lst=[-2,1,-3,4,-1,2,1,-5,4]
sum=0
cur=maxi=lst[0]
for i in lst:
    cur=max(i,cur+i)
    maxi=max(maxi,cur)
print(maxi)