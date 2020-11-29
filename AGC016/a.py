s = input()
alphabets = dict()
for i in s:
    if i not in alphabets:
        alphabets[i] = 1
    else:
        alphabets[i] += 1


if len(alphabets) == 1:
    res = 0
else:
    res = 100
    for key in alphabets.keys():
        shat = s
        for cnt in range(1, 100):
            flag = True
            tmp = ""
            for i in range(1, len(shat)):
                if shat[i - 1] == key or shat[i] == key:
                    tmp += key
                else:
                    tmp += s[i - 1]
                    flag = False
            shat = tmp
            if flag:
                res = min(res, cnt)
                break

print(res)
