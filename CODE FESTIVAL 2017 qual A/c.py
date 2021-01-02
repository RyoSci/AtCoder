s = input()
n = len(s)
k = int(input())
ans = ""

for i in range(n - 1):
    tmp = 26 + ord("a") - ord(s[i])
    if tmp % 26 <= k:
        ans += "a"
        k -= tmp % 26
    else:
        ans += s[i]

ans += chr(ord("a") + (ord(s[-1]) - ord("a") + k) % 26)

print(ans)
