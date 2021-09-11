import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
s = [int(input()) for _ in range(n)]

m = sum(s)
if m % 10 != 0:
    print(m)
else:
    s.sort()
    for i in range(n):
        if s[i] % 10 != 0:
            print(m-s[i])
            break
    else:
        print(0)
