# Input: s = "PAYPALISHIRING", numRows = 3   Output: "PAHNAPLSIIGYIR"
s = "PAYPALISHIRING"
numRows = 3
step=0
cur=0
ls=['']*numRows
for i in s:
    ls[cur]+=i
    if cur==0:
        step=1
    elif cur==numRows-1:
        step=-1
    cur+=step
print("".join(ls))