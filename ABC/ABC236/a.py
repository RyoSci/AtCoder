import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

s=list(input().strip())
a, b = map(int, input().split())
s[a-1], s[b-1] =s[b-1],s[a-1]

print("".join(s))