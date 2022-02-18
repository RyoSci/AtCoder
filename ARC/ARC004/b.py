n = int(input())
d = [int(input()) for i in range(n)]

d_sum = sum(d)
print(d_sum)

d_max = max(d)
if n == 1:
    print(d_sum)
elif n == 2:
    print(abs(d[0] - d[1]))
else:
    if d_max <= d_sum - d_max:
        print(0)
    else:
        print(abs(d_max - (d_sum - d_max)))

