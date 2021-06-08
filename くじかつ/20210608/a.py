abcd = list(map(int, input().split()))

ans = "No"
for i in range(1 << 4):
    eat = 0
    for j in range(4):
        if i >> j & 1:
            eat += abcd[j]
    if sum(abcd)-eat == eat:
        ans = "Yes"
        break

print(ans)
