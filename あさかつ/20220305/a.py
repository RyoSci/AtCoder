# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

p, q, r = map(int, input().split())
print(sum([p, q, r])-max([p, q, r]))
