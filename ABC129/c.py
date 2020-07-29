n, m = map(int, input().split())

stairs = []
is_continuous = False
for i in range(m):
    stairs.append(int(input()))
    if i > 0 and stairs[i] - 1 == stairs[i - 1]:
        is_continuous = True
        break

if is_continuous:
    print(0)
else:
    countup_num = [0] * (n + 1)
    countup_num[0] = 1
    countup_num[1] = 1
    for i in range(2, n + 1):
        countup_num[i] = (countup_num[i - 1] + countup_num[i - 2]) % 1000000007
    res = 1
    diff = 0
    now = 0
    for i in range(m):
        diff = stairs[i] - now - 1
        now = stairs[i] + 1
        res *= (countup_num[diff]) % 1000000007
        # print(res, now)
    if m == 0:
        res = countup_num[n]
    else:
        diff = n - stairs[-1] - 1
        res *= (countup_num[diff]) % 1000000007

    res %= 1000000007
    # print(countup_num)
    print(res)
