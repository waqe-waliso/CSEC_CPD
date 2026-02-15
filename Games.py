n=int(input())
lis=[]
x=0
for i in range(n):
    h,a=map(int,input().split())
    lis.append([h,a])
for i in range(n):
    for j in range(n):
        if lis[i][0]==lis[j][1]:
            x+=1
print(x)
