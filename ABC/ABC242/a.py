# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

a,b,c,x = list(map(int, input().split()))

if x<=a:
    print(1)
elif a<x<=b:
    print(c/(b-a))
else:
    print(0)