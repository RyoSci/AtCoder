n = int(input())


def f(M, m):
    if M >= 35:
        ans[0] += 1
    if 35 > M >= 30:
        ans[1] += 1
    if 30 > M >= 25:
        ans[2] += 1
    if m >= 25:
        ans[3] += 1
    if m < 0 and M >= 0:
        ans[4] += 1
    if M < 0:
        ans[5] += 1

    return


ans = [0] * 6
for i in range(n):
    M, m = map(float, input().split())
    f(M, m)

print(*ans)
