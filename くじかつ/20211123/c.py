import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
s = input().strip()

x = (2+n+3-1)//3
t = "110"*x

cnt = 0
if t[0:n] == s:
    cnt += 1
if t[1:n+1] == s:
    cnt += 1
if t[2:n+2] == s:
    cnt += 1

ans = (10**10-(x-1))*cnt
print(ans)
