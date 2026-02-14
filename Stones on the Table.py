n=int(input())
s=input()
x=0
for i in range(1,n):
    if s[i]==s[i-1]:
        x+=1
print(x)
