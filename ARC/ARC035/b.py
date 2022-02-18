n = int(input())
t = [int(input()) for _ in range(n)]
t.sort()

permitations = 1
mod = 10 ** 9 + 7
cnt = 1
for i in range(n - 1):
    if t[i] == t[i + 1]:
        cnt += 1
        permitations = (permitations * cnt) % mod
    else:
        cnt = 1


for i in range(n - 1):
    t[i + 1] = t[i] + t[i + 1]
penalty = sum(t)

print(penalty)
print(permitations)
