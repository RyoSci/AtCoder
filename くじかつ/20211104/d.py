import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

res = 1
cnt = [0]*(n+1)
cnt[0] = 3

mod = 10**9+7
for i in range(n):
    res *= cnt[a[i]]
    res %= mod
    cnt[a[i]] -= 1
    cnt[a[i]+1] += 1

print(res)
