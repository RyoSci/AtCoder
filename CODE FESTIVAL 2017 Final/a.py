s = input()

ans = "NO"
if len(s) <= 9:
    for i in range(1 << len(s) + 1):
        tmp_s = ""
        for j in range(len(s)):
            if i >> j & 1:
                tmp_s += "A"
            tmp_s += s[j]
        if i >> len(s) & 1:
            tmp_s += "A"
        if tmp_s == "AKIHABARA":
            ans = "YES"
            break

print(ans)
