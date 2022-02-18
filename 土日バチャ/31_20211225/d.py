import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, k = map(int, input().split())
p = list(map(int, input().split()))

ans=0
for i in range(k):
    ans+=p[i]+1

now=ans
for i in range(k,n):
    now+=p[i]+1
    now-=p[i-k]+1
    ans=max(ans,now)

print(ans/2)