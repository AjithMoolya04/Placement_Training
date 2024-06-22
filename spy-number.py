#write a program to spy of the number
num=int(input('enter the number \n'))
temp=num
sum=0
p=1
while(num>0):
    t=num%10
    sum=sum+t
    p=p*t
    num=num//10
if (sum==p):
    print(temp,"is a spy  number!")
else:
    print(temp,"is spy  number")
