n = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split()))

min_id = -1
min_num = 10**10
for i in range(n):
    if t[i] < min_num:
        min_num = t[i]
        min_id = i

ans = [0]*n
ans[min_id] = min_num

for i in range(1, n):
    ans[(i+min_id) % n] = min(ans[(i-1+min_id) %
                                  n]+s[(i-1+min_id) % n], t[(i+min_id) % n])

for i in range(n):
    print(ans[i])
