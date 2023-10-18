# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)

INF = 10**18

n, k = map(int, input().split())

if k == 1:
    a = [0]*n
    for i in range(n):

        print(f"? {i+1}", flush=True)
        t = int(input())
        a[i] = t

    print("!", *a, flush=True)
    exit()


a = [-1]*n
b = [-1]*n
a[0] = 1
b[0] = 0
ks = list(range(1, n+1))
print(f"? {1}", *ks[n-k+1:], flush=True)
t0 = int(input())

for i in range(1, n-k+1):
    print(f"? {i+1}", *ks[n-k+1:], flush=True)
    t = int(input())

    if t0 != t:
        a[i+1] = a[0] ^ 1
        b[i+1] = b[0] ^ 1
    else:
        a[i+1] = a[0]
        b[i+1] = b[0]


t1 = a[0]+a[1]+t0
t1 %= 2

for i in range(n-k+1, n-1):
    print(f"? {1} {2}", *ks[i+1:], flush=True)
    t = int(input())

    if t1 != t:
        a[i] = 1
        b[i] = 1
    else:
        a[i] = 0
        b[i] = 0

asum = sum(a[:k]) % 2
bsum = sum(b[:k]) % 2

if t0 == asum:
    print("!", *a, flush=True)
else:
    print("!", *b, flush=True)
exit()
