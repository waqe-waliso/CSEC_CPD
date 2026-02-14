s=input()
p=s.lower()
u=s.upper()
x=0
for i in range(len(s)):
    if s[i]==p[i]:
        x+=1
y=len(s)-x
if x>=y:
    print(p)
else:
    print(u)
