import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

x = input().strip()

flag = False
ans = []
for i in x:
    if i == "0":
        flag = True
    if flag:
        ans.append("1")
    else:
        ans.append(i)

print("".join(ans))
