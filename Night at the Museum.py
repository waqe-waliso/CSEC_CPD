s=input()
c='a'
t=0
for l in s:
    d=abs(ord(l)-ord(c))
    t+=min(d,26-d)
    c=l
print(t)
