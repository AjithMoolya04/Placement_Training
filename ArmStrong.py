#write program  if n is armstrong or not 
num=int(input("enter the number\n"))
order=len(str(num))
sum=0
temp=num

while temp>0:
    digit=temp%10
    sum+=digit**order
    temp//=10
if num==sum:
    print(num,"is an armstrong number")
else:
    print(num,"ia not an armstrong number")