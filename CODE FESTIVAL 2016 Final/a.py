h, w = map(int, input().split())
for i in range(h):
    s = input().split()
    for j in range(w):
        if s[j] == "snuke":
            ans = chr(ord("A") + j) + str(i + 1)

print(ans)
