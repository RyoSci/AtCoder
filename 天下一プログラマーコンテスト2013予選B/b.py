q, l = map(int, input().split())
num = 0
# q_all = [["Push", 10**2, 2**20] for _ in range(q)]
q_all = [input().split() for _ in range(q)]
stack = []
for i in range(q):
    query = q_all[i]
    if query[0] == "Push":
        if num + int(query[1]) > l:
            print("FULL")
            exit()
        stack.append([num, num+int(query[1]), query[2]])
        num += int(query[1])
        # first = query[2]
    elif query[0] == "Pop":
        if num - int(query[1]) < 0:
            print("EMPTY")
            exit()
        num -= int(query[1])
        # while True:
        while int(query[1]) > 0:
            s, e, t = stack.pop()
            if int(query[1]) >= e-s:
                # if int(query[1]) > e-s:
                query[1] = int(query[1])-(e-s)
                # continue
            else:
                # stack.append([s, s+int(query[1]), t])
                stack.append([s, s+e-s-int(query[1]), t])
                query[1] = 0
                # break
        # first = t
    elif query[0] == "Top":
        if num == 0:
            print("EMPTY")
            exit()
        else:
            # print(first)
            print(stack[-1][2])
    else:
        print(num)
else:
    print("SAFE")
