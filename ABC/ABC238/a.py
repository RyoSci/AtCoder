from math import log2
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
if n > 2*log2(n):
    print("Yes")
else:
    print("No")
