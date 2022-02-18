a = sorted(list(map(int, input().split())))
if a[2]-a[1] == a[1]-a[0]:
    ans = "Yes"
else:
    ans = "No"

print(ans)
