k = int(input())

cnt = 0


def cal(x):
    global cnt
    tmp = 0
    for i in range(1, int(x**0.5)+1):
        cnt += 1
        if x % i == 0:
            tmp += 1
            if x // i != i:
                tmp += 1
    return tmp


memo = [0]*(k+1)
for i in range(1, k+1):
    memo[i] = memo[i-1]+cal(i)
print(cnt)

res = 0
for c in range(1, k+1):
    k_ = k//c
    res += memo[k_]

print(res)
