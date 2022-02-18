n, a, b, c, d = map(int, input().split())
s = input()


def proceed(start, finish):
    global ans
    i = start
    d = finish
    while i < d:
        for j in range(1, 3):
            if s[i + j - 1] == ".":
                i += j
                break
        else:
            ans = "No"
            break


if c < d:
    ans = "Yes"
    proceed(b, d)

    proceed(a, c)

else:
    can_skip = False
    tmp = ""
    for i in range(b - 2, d):
        if s[i] == ".":
            tmp += "."
        else:
            tmp = ""
        if tmp == "...":
            can_skip = True

    if can_skip:
        ans = "Yes"
        proceed(a, c)

        proceed(b, d)

    else:
        ans = "Yes"
        proceed(b, d)

        s = s[:d - 1] + "#" + s[d:]
        proceed(a, c)

print(ans)
