import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

a, b = input().strip().split(".")
a = int(a)

if int(b[0]) >= 5:
    a += 1

print(a)
