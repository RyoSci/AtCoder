# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())

nine = list(map(str, range(1, 10)))
ten = list(map(str, range(10)))

tot = []
for s12 in nine:
    for s3 in ten:
        for s4 in ten:
            for s56 in ten:
                for s79 in ten:
                    for s8 in ten:
                        tmp = s12*2+s3+s4+s56*2+s79+s8+s79
                        tmp = int(tmp)
                        tot.append(tmp)

tot.sort()
print(tot[n-1])
