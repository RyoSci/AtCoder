import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, x, a, b = map(int, input().split())

if n < x:
    print(a*n)
else:
    print(b*n)
