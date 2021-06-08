from itertools import permutations
n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

cnt = 0
for i in permutations(range(1, n+1)):
    cnt += 1
    tmp = list(i)
    if tmp == p:
        a = cnt
    if tmp == q:
        b = cnt

print(abs(a-b))
