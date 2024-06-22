# def power(n,p):
#     if p==0:
#         return 1
#     return (n*power(n,p-1))
# n=2
# p=5
# print(power(n,p))


def power(n,p):
    if(p==1):
        return  n
    temp=pow(n,p/2)
    return temp*temp
n=2
p=4
print(power(n,p))