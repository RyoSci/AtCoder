# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18
n = int(input())

s = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"

print("3." + s[:n])
