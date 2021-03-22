n, m = map(int, input().split())
ans = (m + 1) % n
if ans == 0:
    ans = n

print(ans)
