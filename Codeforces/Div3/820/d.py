from collections import Counter
d = Counter()
b = 2
cnt = 0
while cnt < 50:
    flag = True
    a = 1
    while a < b:
        print("?", a, b, flush=True)
        cnt += 1
        q0 = int(input())
        if q0 == 0:
            break
        print("?", b, a, flush=True)
        cnt += 1
        q1 = int(input())
        if q1 == 0:
            break
        if q0+q1 not in d:
            d[q0+q1] = 0
        d[q0+q1] += 1
        flag = False
        a += 1
    if flag:
        break
    else:
        b += 1

# print(d, flush=True)
print("!", d.most_common()[0][0], flush=True)
