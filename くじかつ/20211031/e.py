import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = input().strip()
n = n[::-1]
res = 0
pre = 0
for i in n:
    if pre+int(i) >= 6:
        res += 10-(pre+int(i))
        pre = 1
    else:
        res += pre+int(i)
        pre = 0
    print(res, pre)
print(res+pre)
