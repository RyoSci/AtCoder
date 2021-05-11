n, k = map(int, input().split())
a = list(map(int, input().split()))
cnt_map = dict()

r = 0
l = 0
res = 0
while r < n:
    if a[r] not in cnt_map:
        cnt_map[a[r]] = 1
    else:
        cnt_map[a[r]] += 1

    while len(cnt_map) > k:
        cnt_map[a[l]] -= 1
        if cnt_map[a[l]] == 0:
            del cnt_map[a[l]]
        l += 1
    res = max(res, r-l+1)
    r += 1

print(res)
