from itertools import permutations
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = input().strip()

res = 0
for i in permutations(n):
    for j in range(1, len(n)):
        l = int("".join(i[:j]))
        r = int("".join(i[j:]))
        res = max(res, l*r)

print(res)
