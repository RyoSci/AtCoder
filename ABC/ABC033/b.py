n = int(input())
max_s = ""
max_pop = 0
sum_pop = 0
for i in range(n):
    s, p = input().split()
    p = int(p)
    sum_pop += p
    if p > max_pop:
        max_pop = p
        max_s = s

if max_pop * 2 > sum_pop:
    print(max_s)
else:
    print("atcoder")
