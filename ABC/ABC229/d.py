import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

s = input().strip()
n = len(s)
k = int(input())

cnt = 0
if k != 0:
    for i in range(n):
        if s[i] == ".":
            cnt += 1
        if cnt == k:
            break

    l = 0
    r = i
    ans = r-l+1
else:
    ans = 0
    tmp = 0
    for l in range(n-1):
        if s[l] == s[l+1] and s[l] == "X":
            tmp += 1
        else:
            ans = max(ans, tmp)
            tmp = 0
    ans = max(ans, tmp)
    if ans != 0:
        print(ans+1)
    else:
        if "X" in s:
            print(1)
        else:
            print(0)
    exit()

for l in range(n-1):
    while r < n-1 and cnt <= k:
        r += 1
        if s[r] == "X":
            continue
        else:
            if cnt < k:
                cnt += 1
                continue
            else:
                r -= 1
                break

    ans = max(ans, r-l+1)
    if s[l] == ".":
        cnt = max(-1, cnt-1)

print(ans)
