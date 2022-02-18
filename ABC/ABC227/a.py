import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, k, a = map(int, input().split())

res = (a+k-1) % n
if res == 0:
    res = n

print(res)
