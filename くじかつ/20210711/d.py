n = int(input())
a = sorted(list(map(int, input().split())), reverse=True)

cor = []
for i in range(n-1, -1, -2):
    cor.append(i)
    cor.append(i)

if n % 2 == 1:
    cor = cor[:n]

if a == cor:
    ans = pow(2, n//2, 10**9+7)
else:
    ans = 0

print(ans)
