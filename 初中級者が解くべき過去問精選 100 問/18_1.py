n = int(input())
s = set(map(int, input().split()))
q = int(input())
t = list(map(int, input().split()))


res = 0
for ti in t:
    if ti in s:
        res += 1

print(res)
