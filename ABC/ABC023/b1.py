n = int(input())
s = input()

ans = -1
abc = "abc"
if n % 6 == 1 and s[0] == "b" or n % 6 == 3 and s[0] == "a" or n % 6 == 5 and s[0] == "c":
    now = s[0]
    for i in range(1, n):
        if s[i] != abc[(abc.index(now) + 1) % 3]:
            break
        now = s[i]
    else:
        ans = n // 2

print(ans)
