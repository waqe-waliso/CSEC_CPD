n=int(input())
games = input()
a = games.count("A")
d= games.count("D")
if a > d:
    print("Anton")
elif d > a:
    print("Danik")
else:
    print("Friendship")
