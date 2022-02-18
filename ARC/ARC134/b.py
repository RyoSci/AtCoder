import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
s = list(input().strip())
a = []
for i in range(n):
    a.append([s[i], -i])

a.sort()
now = 0
end = n-1
used = [0]*n
for i in range(n):
    while now < n and i < end:
        if s[i] <= a[now][0]:
            break
        else:
            if i <= -a[now][1] <= end and used[i] == 0 and used[-a[now][1]] == 0:
                end = -a[now][1]-1
                s[i], s[-a[now][1]] = s[-a[now][1]], s[i]
                used[i] = 1
                used[-a[now][1]] = 1
                now += 1
                break
            else:
                now += 1

print("".join(s))
