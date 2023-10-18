# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

s = input()

d = {
    "tourist": 3858,
    "ksun48": 3679,
    "Benq": 3658,
    "Um_nik": 3648,
    "apiad": 3638,
    "Stonefeang": 3630,
    "ecnerwala": 3613,
    "mnbvmar": 3555,
    "newbiedmy": 3516,
    "semiexp": 3481,

}

print(d[s])
