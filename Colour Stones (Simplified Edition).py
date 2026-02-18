s=input()
t=input()
x=1
y=s[0]
for i in range(len(t)):
    if t[i]==y:
        y=s[x]
        x+=1
print(x)
