import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

# a = []
# for i in range(1, 10**4):
#     tmp = i*(i+1)*(i+2)//6
#     if tmp > 10**6:
#         break
#     a.append(tmp)

# n = len(a)
# a = [0]+a


def a(x):
    return x*(x+1)*(x+2)//6


INF = 10**18
dp_odd = [INF]*(10**6+1)
dp_even = [INF]*(10**6+1)
dp_odd[0] = 0
dp_even[0] = 0

# dp_odd = [[INF]*(10**6+1) for _ in range(n+1)]
# dp_even = [[INF]*(10**6+1) for _ in range(n+1)]
# dp_odd[0][0] = 0
# dp_even[0][0] = 0


def chmin(dp, x, y):
    if dp[x] > dp[y]+1:
        dp[x] = dp[y]+1


# i番目まで使用したときの正四面体数の合計がj個である場合の正四面体数の最小個数。
# for i in range(1, n+1):
for i in range(1, 200):
    ai = i*(i+1)*(i+2)//6
    # for j in range(10**3+1):
    for j in range(10**6+1):
        # つかわない
        # dp_even[i][j] = min(dp_even[i-1][j], dp_even[i][j])
        # dp_odd[i][j] = min(dp_odd[i-1][j], dp_odd[i][j])
        if ai % 2 == 0:
            # つかう
            if j+ai <= 10**6:
                # dp_even[i][j+ai] = min(dp_even[i][j+ai], dp_even[i][j]+1)
                # dp_even[j+ai] = min(dp_even[j+ai], dp_even[j]+1)
                # chmin(dp_even, j+ai, j)
                if dp_even[j+ai] > dp_even[j]+1:
                    dp_even[j+ai] = dp_even[j]+1
        else:
            # つかう
            if j+ai <= 10**6:
                # dp_odd[i][j+ai] = min(dp_odd[i][j+ai], dp_odd[i][j]+1)
                # dp_even[i][j+ai] = min(dp_even[i][j+ai], dp_even[i][j]+1)
                # dp_odd[j+ai] = min(dp_odd[j+ai], dp_odd[j]+1)
                # dp_even[j+ai] = min(dp_even[j+ai], dp_even[j]+1)
                # chmin(dp_odd, j+ai, j)
                # chmin(dp_even, j+ai, j)
                if dp_odd[j+ai] > dp_odd[j]+1:
                    dp_odd[j+ai] = dp_odd[j]+1
                if dp_even[j+ai] > dp_even[j]+1:
                    dp_even[j+ai] = dp_even[j]+1


ans = []
for i in range(10**8):
    q = int(input())
    if q == 0:
        break
    ans.append([dp_even[q], dp_odd[q]])


for even, odd in ans:
    print(even, odd)
