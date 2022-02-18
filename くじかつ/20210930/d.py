import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

s = input().strip()
n = len(s)

ans = 0
for i in range(1 << n-1):
    tmp = s[0]
    res = 0
    for j in range(n-1):
        if i >> j & 1:
            res += int(tmp)
            tmp = s[j+1]
        else:
            tmp += s[j+1]
    res += int(tmp)
    ans += res
print(ans)
