# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
# 文字列入力の時は空白区切りでないかチェック
s = input()
t = [0]*3

for i in range(n):
    if s[i] == "A":
        t[0] = 1
    if s[i] == "B":
        t[1] = 1
    if s[i] == "C":
        t[2] = 1

    if sum(t) == 3:
        print(i+1)
        exit()
