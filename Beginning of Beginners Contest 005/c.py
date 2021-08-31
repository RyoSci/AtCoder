import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()

res = max(abs(a[0]-b[-1]), abs(a[-1]-b[0]))
print(res)
