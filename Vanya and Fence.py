n,h = map(int,input().split())
a = list(map(int,input().split()))
sum = 0
for i in range(n):
    if a[i] <= h:
        sum+=1
    else:
        sum+=2
print(sum)
