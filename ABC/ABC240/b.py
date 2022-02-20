import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
a = set(map(int, input().split()))

print(len(a))