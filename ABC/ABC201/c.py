s = input()

o = []
x = []
q = []

for i in range(10):
    if s[i] == "o":
        o.append(i)
    elif s[i] == "x":
        x.append(i)
    else:
        q.append(i)


def check_o(i):
    for j in o:
        if not str(j) in i:
            return 0
    return 1


def check_q(i):
    for j in i:
        j = int(j)
        if not (j in o or j in q):
            return 0
    return 1


res = 0
for i in range(10**4):
    i = str(i)
    i = (4-len(i))*"0"+i
    if check_o(i) and check_q(i):
        res += 1

print(res)
