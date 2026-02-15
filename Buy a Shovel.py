k,r=map(int,input().split())
def fun(a,b):
    n=0
    while (n*a-b)%10!=0:
        n+=1
        if (n*a)%10==0:
            return n
    return n
    
print(fun(k,r))
