# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans0=0
ans1=0
for i in range(n):
    if a[i]==b[i]:
        ans0+=1
    else:
        if b[i] in a:
            ans1+=1

print(ans0)
print(ans1)