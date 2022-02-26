import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

memo = [-1]*(n+1)
cnt = [0]*(2*n)

x = 0
for i in range(k):
    if memo[x % n] != -1:
        cycle_start = memo[x % n]
        before_cycle = cnt[cycle_start]
        cycle_cnt = cnt[i]-cnt[memo[x % n]]
        cycle_num = i-memo[x % n]
        break
    memo[x % n] = i
    x += a[x % n]
    cnt[i+1] = x
else:
    print(x)
    exit()

ans = before_cycle
if k-cycle_start >= 0:
    ans += (k-cycle_start)//cycle_num*cycle_cnt
    k = (k-cycle_start) % cycle_num

for i in range(k):
    ans += a[x % n]
    x += a[x % n]

print(ans)
