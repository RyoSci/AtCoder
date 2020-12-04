s = input()
a = ord("a")
ans = "-1"
for i in range(26):
    if chr(a + i) not in s:
        ans = s + chr(a + i)
        break

if ans != "-1":
    print(ans)
else:
    s_set = set(s)
    for i in range(len(s) - 1, -1, -1):
        j = 1
        while ord(s[i]) + j <= ord("z"):
            if chr(ord(s[i]) + j) not in s_set:
                ans = s[:i] + chr(ord(s[i]) + j)
                break
            j += 1
        else:
            s_set.remove(s[i])
        if ans != "-1":
            break

    print(ans)
