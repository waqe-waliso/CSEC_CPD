
a1,a2,a3,a4=map(int,input().split())
s=input()
c=0
for i in range(len(s)):
    if s[i]=='1':
        c+=a1
    elif s[i]=='2':
        c+=a2
    elif s[i]=='3':
        c+=a3
    else:
        c+=a4
print(c)
