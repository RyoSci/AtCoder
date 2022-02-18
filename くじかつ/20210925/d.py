import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

s = input().strip()
s = s.replace("BC", "D")
res = 0

now = 0
for i in s:
    if i == "A":
        now += 1
    elif i == "D":
        res += now
    else:
        now = 0

print(res)
