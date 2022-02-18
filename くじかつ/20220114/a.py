import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

a, b, t = list(map(int, input().split()))
print(t//a*b)
