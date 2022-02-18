import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
if n >= 42:
    n += 1
print("AGC"+str(n).zfill(3))
