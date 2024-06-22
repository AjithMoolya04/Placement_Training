# write program, if the number is strong number
num=int(input("enter the number\n"))
sum=0
temp=num
while(num):
    i=1
    f=1
    r=num%10
    while(i<=r):
        f=f*i
        i=i*1
    sum=sum+f
    num=num//10
if temp==sum:
    print("the number is strong")
else:
    print("the number is not strong number")