import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, d = map(int, input().split())
lr = [list(map(int, input().split()))+[i] for i in range(n)]

lr_tail = sorted(lr, key=lambda x: x[1])
lr_head = sorted(lr, key=lambda x: x[0])

ans = 0
seen = set()
j = 0
for i in range(n):
    _, r, ii = lr_tail[i]
    if ii in seen:
        continue
    ans += 1
    seen.add(ii)
    while j < n:
        ll, rr, iii = lr_head[j]
        if iii in seen:
            j += 1
        elif ll <= r+d-1:
            j += 1
            seen.add(iii)
        else:
            break

print(ans)
