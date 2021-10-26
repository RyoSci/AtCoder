import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

s = input().strip()
cnt = 0
for i in s:
    if i == "o":
        cnt += 1
cnt += 15-len(s)

if cnt >= 8:
    print("YES")
else:
    print("NO")
