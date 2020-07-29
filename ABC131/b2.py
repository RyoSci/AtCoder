n ,l = map(int, input().split())
apple = []
for i in range(n):
    apple.append(l + i)

if l - 1 + n - 1 < 0:
    print(sum(apple[:n - 1]))
elif l < 0 and  0 <= l - 1 + n - 1:
    print(sum(apple))
elif 0 <= l:
    print(sum(apple[1:]))