n, k = map(int, input().split())
t = [list(map(int, input().split())) for i in range(n)]
for i in range(k ** n):
    ans = t[0][i % k]
    i //= k
    for j in range(1, n):
        ans ^= t[j][i % k]
        i //= k
    if ans == 0:
        print("Found")
        break
else:
    print("Nothing")
