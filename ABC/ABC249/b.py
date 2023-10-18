# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from curses.ascii import islower, isupper
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

# 文字列入力の時は空白区切りでないかチェック
s = input()

is_l = False
is_s = False
is_d = True
d = dict()

for c in s:
    if isupper(c):
        is_l = True
    elif islower(c):
        is_s = True

    if c not in d:
        d[c] = 0
    else:
        is_d = False

if is_l and is_s and is_d:
    print("Yes")
else:
    print("No")
