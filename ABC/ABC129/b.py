n = int(input())
w = list(map(int, input().split()))
sum_w = sum(w)
res = 10**6
count_up = 0
for i in range(n):
    count_up += w[i]
    sum_w -= w[i]
    if abs(sum_w - count_up) < res:
        res = abs(sum_w - count_up)
print(res)
    
