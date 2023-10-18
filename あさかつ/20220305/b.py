# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = input().strip()

if n == n[::-1]:
    print("Yes")
    exit()
m = len(n)
a = 0
b = 0
for i in range(m):
    if n[i] == '0':
        a += 1
    else:
        break

for i in range(m-1, -1, -1):
    if n[i] == '0':
        b += 1
    else:
        break

if a <= b and n[a:m-b] == n[a:m-b][::-1]:
    print("Yes")
else:
    print("No")
