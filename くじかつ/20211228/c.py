import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
a = (1900*m+100*(n-m))*pow(1/2, m)
b = 1-pow(1/2, m)
print(int(a/(1-b)**2))
