# write a program to check if  number is happy  number or  not

def ishappy(num):
    r=0
    while(num!=0):
        d=num%10
        r+=d**2
        num=num//10
    return r
num=int(input("enter the number "))
res=num

while(res!=1 and res!=4):
    res=ishappy(res)

if(res==1):
    print("happay number ")
else:
    print("not a happy number")