n=int(input())
a=list(map(int,input().split()))
m=int(input())
for i in range(m):
    x,y=map(int,input().split())
    if x==1:
        a[x]+=(a[x-1]-y)
        
    elif x==n:
        a[x-2]+=(y-1)
    else:
        a[x]+=(a[x-1]-y)
        a[x-2]+=(y-1)
    a[x-1]=0
for i in range(n):
     print(a[i])
