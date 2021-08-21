n = int(input())
a = list(map(int, input().split()))
four = 0
two = 0
for i in range(n):
    if a[i] % 4 == 0:
        four += 1
    elif a[i] % 2 == 0:
        two += 1

if four*2+1 >= n:
    ans = "Yes"
elif four*2+two >= n:
    ans = "Yes"
else:
    ans = "No"

print(ans)
