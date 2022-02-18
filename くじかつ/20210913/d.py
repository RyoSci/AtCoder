import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

s = list(input().strip())
k = int(input())

n = len(s)

res = []

for i in range(n-1):
    tmp = (ord("a")-ord(s[i])) % 26
    if tmp > k:
        res.append(s[i])
        continue
    k -= tmp
    res.append("a")


res.append(chr((ord(s[n-1])-ord("a")+k % 26) % 26 + ord("a")))

print(*res, sep="")
