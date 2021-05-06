h, w = map(int, input().split())
if h >= 2 and w >= 2:
    ans = ((h+1)//2) * ((w+1)//2)
else:
    ans = h*w

print(ans)
