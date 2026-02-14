n=int(input())
lis=list(map(int,input().split()))
s=0
d=0
while len(lis)!=0:
    a=max(lis[0],lis[len(lis)-1])
    s+=a
    lis.remove(a)
    if len(lis)!=0:
        a=max(lis[0],lis[len(lis)-1])
        d+=a
        lis.remove(a)
print(s,d)
