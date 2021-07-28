s = input()

c = ""
for i in s:
    if i != "x":
        c += i

if c != c[::-1]:
    print(-1)
else:
    l = 0
    r = len(s)-1
    ans = 0
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        elif s[l] == "x":
            ans += 1
            l += 1
        elif s[r] == "x":
            ans += 1
            r -= 1
    print(ans)
