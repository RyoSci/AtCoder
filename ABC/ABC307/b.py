# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
s = []
for i in range(n):
    si = input()
    s.append(si)

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        tmp = s[i] + s[j]

        if tmp == tmp[::-1]:
            print("Yes")
            exit()
print("No")
