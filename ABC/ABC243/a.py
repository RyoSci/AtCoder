# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

v, a, b, c = list(map(int, input().split()))

for i in range(10**6):
    if v-a >= 0:
        v -= a
    else:
        print("F")
        exit()

    if v-b >= 0:
        v -= b
    else:
        print("M")
        exit()

    if v-c >= 0:
        v -= c
    else:
        print("T")
        exit()
