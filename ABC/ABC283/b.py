# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
input=lambda: sys.stdin.readline().rstrip()
INF = 10**18

n = int(input())
a = list(map(int, input().split()))
q = int(input())
ans=[]
for i in range(q):
    l = list(map(int, input().split()))
    if l[0] == 1:
        k,x = l[1:]
        k-=1
        a[k]=x
    else:
        k = l[1]
        k-=1
        ans.append(a[k])

print(*ans)