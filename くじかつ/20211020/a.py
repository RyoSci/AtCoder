import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
print(n*800-n//15*200)
