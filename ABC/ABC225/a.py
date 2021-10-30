from itertools import permutations
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


s = input().strip()

res = set(permutations(s))

print(len(res))
