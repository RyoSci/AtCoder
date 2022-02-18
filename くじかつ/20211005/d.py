import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

s = input().strip()
n = len(s)
aa = []
for i in range(n-2):
    if s[i] == s[i+1] and s[i+1] != s[i+2]:
        aa.append([s[i], i])

d = [[0]*(n+1) for _ in range(26)]

for i in range(n):
    d[ord(s[i])-ord("a")][i+1] += 1
    for j in range(26):
        d[j][i+1] += d[j][i]

m = len(aa)
res = 0
for i in range(m-1, -1, -1):
    si, index = aa[i]
    if i == m-1:
        res += n-1-(index+1)-(d[ord(si)-ord("a")][n] -
                              d[ord(si)-ord("a")][index+2])
    else:
        nsi, nindex = aa[i+1]
        if si != nsi:
            res += n-1-(index+1)-(d[ord(si)-ord("a")][nindex] -
                                  d[ord(si)-ord("a")][index+2])
        else:
            res += nindex-1 - \
                (index+1) - (d[ord(si)-ord("a")][nindex] -
                             d[ord(si)-ord("a")][index+2])

print(res)
