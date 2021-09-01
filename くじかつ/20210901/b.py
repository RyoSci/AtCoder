import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

s = int(input())

d = set()

for i in range(10**7):
    if s not in d:
        d.add(s)
    else:
        break
    if s % 2 == 0:
        s //= 2
    else:
        s = 3*s+1

print(i+1)
