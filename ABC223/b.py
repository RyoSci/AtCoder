from abc import abstractproperty
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

s = input().strip()

n = len(s)

t = []
for i in range(n):
    t.append(s[i:]+s[:i])

t.sort()
print(t[0])
print(t[-1])
