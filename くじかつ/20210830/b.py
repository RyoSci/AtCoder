import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

if n == len(set(a)):
    print("YES")
else:
    print("NO")
