n, m, k = map(int, input().split())
s = [input() for i in range(n)]

res = 1
for i in range(min(n, m), 1, -1):
    for w in range(n - i + 1):
        for h in range(m - i + 1):
            counter = [0] * 10
            for dw in range(i):
                for dh in range(i):
                    tmp = int(s[w + dw][h + dh])
                    counter[tmp - 1] += 1
            if max(counter) >= i * i - k:
                res = i
                break
        if res != 1:
            break
    if res != 1:
        break

print(res)
