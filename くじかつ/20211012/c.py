import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

s = input().strip()
n = len(s)

if n <= 25:
    for i in range(26):
        c = chr(ord("a")+i)
        if c not in s:
            print(s+c)
            exit()
else:
    d = []
    for i in range(n-1, -1, -1):
        for j in range(len(d)):
            if ord(d[j]) > ord(s[i]):
                print(s[:i]+d[j])
                exit()
        d.append(s[i])
    else:
        print(-1)
