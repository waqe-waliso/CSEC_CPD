n=int(input())
lis=list(map(int,input().split()))
a=0
p=0
for v in lis:
    if v==-1 and p==0:
        a+=1
    else:
        if v==-1:
            p-=1
        elif v!=-1:
            p+=v
print(a)
