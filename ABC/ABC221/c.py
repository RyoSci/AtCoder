import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = input().strip()
m = len(n)

res = 0
for i in range(1, 2**m-1):
    l = []
    r = []
    for j in range(m):
        if i >> j & 1:
            l.append(n[j])
        else:
            r.append(n[j])
    l.sort(reverse=True)
    r.sort(reverse=True)
    l_num = int("".join(l))
    r_num = int("".join(r))

    if l_num == 0 or r_num == 0:
        continue
    res = max(res, l_num*r_num)

print(res)
