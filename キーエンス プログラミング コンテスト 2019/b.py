s = input()
keyence = "keyence"
ans = "NO"
for i in range(8):
    l = keyence[:i]
    r = keyence[i:]
    if s[:i] == l and s[len(s) - (7 - i):] == r:
        ans = "YES"

print(ans)
