import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

p = list(map(int, input().split()))

res = ""
for i in p:
    res += chr(i-1+ord("a"))

print(res)
