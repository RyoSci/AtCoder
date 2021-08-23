from itertools import permutations
import sys
sys.setrecursionlimit(10**7)

s, k = input().split()
k = int(k)
s = sorted(list(s))
t = list(permutations(s))

d = dict()
cnt = 0
for i in t:
    tmp = "".join(i)
    if tmp not in d:
        cnt += 1
        d[tmp] = 1
    if cnt == k:
        print(tmp)
        break
