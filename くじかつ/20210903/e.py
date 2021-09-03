import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())

d = dict()


def cal(x):
    i = 2
    while x > 1:
        if x % i == 0:
            x //= i
            if i not in d:
                d[i] = 0
            d[i] += 1
        else:
            i += 1


res = 0
for i in range(1, n+1):
    cal(i)

cnt = [0]*100
for key, val in d.items():
    for i in range(1, val+1):
        cnt[i] += 1

res += cnt[4]*(cnt[4]-1)//2*(cnt[2]-2)
res += cnt[24]*(cnt[2]-1)
res += cnt[14]*(cnt[4]-1)
res += cnt[74]


print(res)
