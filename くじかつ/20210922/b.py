import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

x = input().rstrip()
x_orderd = [0]*26
for i in range(26):
    x_orderd[ord(x[i]) - ord("a")] = i

n = int(input())
res = []
for i in range(n):
    s = input().rstrip()
    tmp = ""
    for j in s:
        tmp += chr(x_orderd[ord(j)-ord("a")]+ord("a"))
    res.append([tmp, s])

res.sort()
for i in range(n):
    print(res[i][1])
