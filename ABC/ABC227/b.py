import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

total=set()
for a in range(1,1000):
    for b in range(1,1000):
        total.add(4*a*b+3*a+3*b)

n = int(input())
s = list(map(int, input().split()))

res=0
for i in range(n):
    if s[i] not in total:
        res+=1

print(res)