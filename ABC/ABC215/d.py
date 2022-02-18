import sys
sys.setrecursionlimit(10**7)
n, m = map(int, input().split())
a = list(map(int, input().split()))
ans = [1]*(m+1)
ans[0] = 0

b = [0]*(10**5+1)


def cal(x):
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            b[i] = 1
            b[x//i] = 1
    return


for i in range(n):
    cal(a[i])
b[1] = 0


for i in range(10**5+1):
    if b[i] == 0:
        continue
    for j in range(i, m+1, i):
        ans[j] = 0


res = 0
ans_ = []
for i in range(m+1):
    if ans[i] == 1:
        res += 1
        ans_.append(i)

print(res)
print(*ans_, sep="\n")
