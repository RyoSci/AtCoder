import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

if -pow(2, 31) <= n < pow(2, 31):
    print("Yes")
else:
    print("No")
