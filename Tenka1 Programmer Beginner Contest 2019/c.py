n = int(input())
s = input()
w = 0
b = 0
ans = 0
for i in range(n - 1, -1, -1):
    if s[i] == ".":
        w += 1
    else:
        b += 1
        if b >= w:
            ans += w
            w = 0
            b = 0
if w > 0:
    ans += b

print(ans)
