def fabi(n):
    if(n<=1):
        return n
    else:
        return fabi(n-1)+fabi(n-2)
    
print("fabinacii number is: ",fabi(6))