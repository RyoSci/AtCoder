n = int(input())
e = list(map(int, input().split()))


def cal(x):
    tmp = []
    while x > 0:
        tmp.append(x % 3)
        x //= 3
    return [0]*(n-len(tmp))+tmp[::-1]


ans = "No"
for i in range(3**n):
    tmp = cal(i)
    cnt = [0]*3
    for j in range(n):
        if tmp[j] == 0:
            cnt[0] += e[j]
        elif tmp[j] == 1:
            cnt[1] += e[j]
        else:
            cnt[2] += e[j]
    if cnt[0] == cnt[1] and cnt[1] == cnt[2]:
        ans = "Yes"
        break

print(ans)
