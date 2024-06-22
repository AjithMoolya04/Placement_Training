#write a program to check if number is neon number or not
num=int(input("enter the number\n"))
sq=num*num
temp=num
sum=0

while(sq!=0):
    r=sq%10
    sum=sum+r
    sq=sq//10
if(sum==temp):
    print("neon")
else:
    print("not neon")