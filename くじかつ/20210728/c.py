sa = input()[::-1]
sb = input()[::-1]
sc = input()[::-1]


now = "a"

while 1:
    if now == "a":
        if sa == "":
            print("A")
            break
        else:
            now = sa[-1]
            sa = sa[:-1]
    elif now == "b":
        if sb == "":
            print("B")
            break
        else:
            now = sb[-1]
            sb = sb[:-1]
    elif now == "c":
        if sc == "":
            print("C")
            break
        else:
            now = sc[-1]
            sc = sc[:-1]
