s = input()
t = input()

for i in range(len(s)):
    if s == t:
        ans = i
        break
    else:
        s = s[-1] + s[:-1]
else:
    ans = -1

print(ans)
