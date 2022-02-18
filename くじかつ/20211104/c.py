import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))


def div(x):
    a = x
    for i in range(2, int(a**0.5)+1):
        while 1:
            if x % i == 0:
                x //= i
                s.add(i)
            else:
                break
    if x != 1:
        s.add(x)

    return


s = set()

for i in range(n):
    div(a[i])

table = [1]*(m+1)
for i in s:
    # if i == 1 or table[i] == 0:
    if i == 1:
        continue
    for j in range(i, m+1, i):
        table[j] = 0

res = []
for i in range(1, m+1):
    if table[i] == 1:
        res.append(i)

res.sort()
print(len(res))
print(*res, sep="\n")
