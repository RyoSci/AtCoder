n = int(input())
a = list(map(int, input().split()))
res = 0

now = ""

for i in range(n - 1):
    if a[i + 1] > a[i]:
        if now == "down":
            res += 1
            now = ""
        else:
            now = "up"
    elif a[i + 1] < a[i]:
        if now == "up":
            res += 1
            now = ""
        else:
            now = "down"

print(res + 1)
