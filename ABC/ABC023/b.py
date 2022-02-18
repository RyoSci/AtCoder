n = int(input())
s = input()

res = "b"
ans = -1
for i in range(50):
    if res == s:
        ans = 3 * i
        break
    res = "a" + res + "c"
    if res == s:
        ans = 3 * i + 1
        break
    res = "c" + res + "a"
    if res == s:
        ans = 3 * i + 2
        break
    res = "b" + res + "b"

print(ans)
