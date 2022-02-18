import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

s, t = input().split()
a, b = map(int, input().split())
u = input().strip()

if s == u:
    a -= 1
elif t == u:
    b -= 1

print(a, b)
