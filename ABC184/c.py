r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())


if r1 == r2 and c1 == c2:
    ans = 0
elif r1+c1 == r2+c2 or r1-c1 == r2-c2 or abs(r1-r2)+abs(c1-c2) <= 3:
    ans = 1
elif abs(c2-r2 - (c1-r1)) <= 6:
    ans = 2
elif abs(c2-r2 - (c1-r1)) % 2 == 0:
    ans = 2
elif abs(c2+r2 - (c1+r1)) <= 3:
    ans = 2
else:
    ans = 3

print(ans)
