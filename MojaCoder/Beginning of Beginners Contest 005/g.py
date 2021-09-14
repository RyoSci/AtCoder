from bisect import bisect_left
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

l, r = map(int, input().split())

dp = [0]*100
dp[0] = 1
dp[1] = 1

for i in range(98):
    dp[i+2] = dp[i+1]+dp[i]


def cal(x):
    res = 0
    for i in range(1, 101):
        if x < dp[i]:
            break
        res += i*dp[i-1]
    return res-(dp[i]-x-1)*(i-1)


res = cal(r)-cal(l-1)
print(res)
