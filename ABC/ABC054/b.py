n, m = map(int, input().split())
a = [input() for _ in range(n)]
b = [input() for _ in range(m)]

ans = "No"
for i in range(n - m + 1):
    for j in range(n - m + 1):
        is_break = False
        for ii in range(m):
            for jj in range(m):
                if a[ii + i][jj + j] != b[ii][jj]:
                    is_break = True
                    break
            if is_break:
                break
        else:
            ans = "Yes"
            break
    if ans == "Yes":
        break

print(ans)
