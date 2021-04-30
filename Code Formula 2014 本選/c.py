s = input()
users = dict()


def register(tmp):
    if tmp != "":
        if tmp not in users:
            users[tmp] = 1
        else:
            users[tmp] += 1


has_at = False
tmp = ""
for i in s:
    if i == "@":
        register(tmp)
        tmp = ""
        has_at = True
    elif i == " ":
        register(tmp)
        tmp = ""
        has_at = False
    else:
        if has_at:
            tmp += i

register(tmp)

for key in sorted(users.keys()):
    print(key)
