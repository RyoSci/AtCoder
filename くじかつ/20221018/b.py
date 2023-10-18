# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

abcd = input()


def f(i, res, ans):
    if i == 3:
        if res == 7:
            print(ans+"=7")
            exit()
        return
    f(i+1, res+int(abcd[i+1]), ans+"+"+abcd[i+1])
    f(i+1, res-int(abcd[i+1]), ans+"-"+abcd[i+1])


f(0, int(abcd[0]), abcd[0])
