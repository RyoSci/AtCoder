import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, l, w = list(map(int, input().split()))
a = list(map(int, input().split()))
a = [-w]+a+[l]

ans = 0
for i in range(n+1):
    ans += (max(0, a[i+1]-a[i]-w)+w-1)//w
print(ans)
