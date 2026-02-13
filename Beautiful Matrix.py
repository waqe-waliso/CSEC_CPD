for i in range(5):
    lis = list(map(int,input().split()))
    if 1 in lis:
        n=i
        m=lis.index(1)
answer = abs(2-n)+abs(2-m)
print(answer)
