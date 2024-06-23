def binary(d):
    b=" "
    while(d>0):
        b=str(d%2)+b
        d=d//2
    return b
d=int(input())
print(binary(d))
        

        