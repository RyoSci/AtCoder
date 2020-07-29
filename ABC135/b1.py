n = int(input())
p = list(map(int, input().split()))

swap = 0

for i in range(n):
    min_num = p[i]
    min_j = i
    for j in range(i, n):
        if min_num > p[j]:
            min_num = p[j]
            min_j = j
    if min_j != i:
        p[i] ,p[min_j] = p[min_j], p[i] 
        swap += 1
    # print(swap)
    # print(p)
if swap <= 1:
    print("YES")
else:
    print("NO")
