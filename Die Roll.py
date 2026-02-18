y, w = map(int, input().split())
m = max(y, w)
f = 7 - m
t = 6
g = 1
for i in range(1,f + 1):
    if f % i == 0 and t % i == 0:
        g = i
n = f // g
d = t // g
print(f"{n}/{d}")
