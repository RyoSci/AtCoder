n = int(input())
a = [int(input()) for i in range(n)]
a.sort(reverse=True)
counter = 0
max_num = a[0]
for i in range(n):
    if max_num > a[i]:
        print(a[i])
        break
