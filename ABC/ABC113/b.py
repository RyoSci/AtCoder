n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))

min_tmp = 10 ** 5
index = 0
for i in range(n):
    tmp = abs(a - (t - 0.006 * h[i]))
    if tmp <= min_tmp:
        min_tmp = tmp
        index = i
    # print(tmp)
print(index + 1)
