n = int(input())
a_2b = []

aoki = 0
for i in range(n):
    a, b = map(int, input().split())
    aoki += a
    a_2b.append(b+2*a)

a_2b.sort(reverse=True)

for i in range(n):
    aoki -= a_2b[i]
    if aoki < 0:
        ans = i + 1
        break
print(ans)
