def isAnagram(s, t):
    d1={}
    d2={}
    if len(s)!=len(t):
            return False
    else:
        for i in range(len(s)):
            d1[s[i]]=1+d1.get(s[i],0)
            d2[t[i]]=1+d2.get(t[i],0)
        for k in d1:
            if d1[k]!=d2.get(k,0):
                return False
        return True
s="jar"
t="jam"
print(isAnagram(s,t))