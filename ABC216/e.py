import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))+[0]
a.sort(reverse=True)
now = a[0]
cnt = 1
res = 0

for i in range(1, n+1):
    if k == 0:
        break
    tmp = min((now-a[i])*cnt, k)
    k -= tmp
    div = tmp//cnt
    mod = tmp % cnt
    res += (now+now-div+1)*div//2*cnt
    res += mod*(now-div)
    cnt += 1
    now = a[i]

print(res)
