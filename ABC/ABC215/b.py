import sys
sys.setrecursionlimit(10**7)

n = int(input())
k = 0
while 1:
    if 2**k > n:
        break
    k += 1

print(k-1)
