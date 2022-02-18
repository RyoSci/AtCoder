import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

a,b = input().strip().split("x")

print(int(a)*int(b))