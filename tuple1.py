
# from functools import reduce

def add(x,y):
    return x+y

original=(1,2,3,4,5)

result=reduce(add,original)
print("result of reducing the  tuple",result)