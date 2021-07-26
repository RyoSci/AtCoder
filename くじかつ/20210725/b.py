a, b, k = map(int, input().split())
ans = set()

for i in range(a, a+k):
    if i <= b:
        ans.add(i)

for i in range(b, b-k, -1):
    if a <= i:
        ans.add(i)

ans = sorted(list(ans))
for i in ans:
    print(i)
