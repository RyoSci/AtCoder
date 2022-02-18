n = int(input())
l = list(map(int, input().split()))
l_max = max(l)
sum_l = sum(l) - l_max

if l_max < sum_l:
    print("Yes")
else:
    print("No")