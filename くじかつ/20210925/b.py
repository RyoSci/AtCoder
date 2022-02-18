import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())

for k in range(100):
    if 2**k > n:
        break

print(k-1)
