import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

nwse = [0]*4
NWSE = "NWSE"
s = input().strip()

for i in s:
    for j in range(4):
        if i == NWSE[j]:
            nwse[j] += 1

ans = "No"
if nwse[0] > 0 and nwse[2] > 0 or nwse[0] == 0 and nwse[2] == 0:
    if nwse[1] > 0 and nwse[3] > 0 or nwse[1] == 0 and nwse[3] == 0:
        ans = "Yes"

print(ans)
