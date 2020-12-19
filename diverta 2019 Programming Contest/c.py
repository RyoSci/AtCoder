n = int(input())
ans, ab, a, b = 0, 0, 0, 0
for i in range(n):
    s = input()
    for j in range(len(s) - 1):
        if s[j:j + 2] == "AB":
            ans += 1
    if s[0] == "B" and s[-1] == "A":
        ab += 1
    elif s[0] == "B":
        b += 1
    elif s[-1] == "A":
        a += 1

if ab:
    ans += ab - 1
    if a:
        ans += 1
        a -= 1
    if b:
        ans += 1
        b -= 1

ans += min(a, b)
print(ans)
