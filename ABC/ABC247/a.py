# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
input=lambda: sys.stdin.readline().rstrip()
INF = 10**18

# 文字列入力の時は空白区切りでないかチェック
s = input()
print("0"+s[:3])