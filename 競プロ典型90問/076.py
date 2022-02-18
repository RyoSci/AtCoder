n = int(input())
a = list(map(int, input().split()))
total = sum(a)


def rool(cnt, j):
    for i in range(n):
        cnt += a[i]
        if cnt == total//10:
            print("Yes")
            exit()
        while cnt > total//10:
            cnt -= a[j]
            j = (j+1) % n
    return cnt, j


if total % 10 != 0:
    print("No")
    exit()
else:
    cnt = 0
    j = 0
    cnt, j = rool(cnt, j)
    cnt, j = rool(cnt, j)
    print("No")
