n = int(input())
s = input()
t = input()

cnt = 0
for i in range(1, n + 1):
    if s[::-1][0:i][::-1] == t[0:i]:
        cnt = i

print(2 * n - cnt)
