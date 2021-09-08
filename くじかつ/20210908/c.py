import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

s = input().strip()
n = len(s)

ans = "No"
if n <= 2:
    if int(s) in [8, 16, 61, 24, 42, 32, 23, 48, 84, 56, 65, 64, 46, 72, 27, 88, 96, 69]:
        ans = "Yes"
else:
    d = dict()
    for i in s:
        if i not in d:
            d[i] = 0
        d[i] += 1

    for i in range(112, 1000, 8):
        i = str(i)
        tmp = dict()
        for j in i:
            if j not in tmp:
                tmp[j] = 0
            tmp[j] += 1

        for key, val in tmp.items():
            if key not in d or d[key] < val:
                break
        else:
            ans = "Yes"

print(ans)
