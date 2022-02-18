n = input()

ans = "No"
for i in range(10):
    res = "0" * i + n
    if res == res[::-1]:
        ans = "Yes"
        break

print(ans)
