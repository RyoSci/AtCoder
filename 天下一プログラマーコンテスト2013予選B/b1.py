q, l = map(int, input().split())
num = 0
# q_all = [["Push", 10**2, 2**20] for _ in range(q)]
q_all = [input().split() for _ in range(q)]
stack = []
for i in range(q):
    querry, *s = q_all[i]
    if querry == "Push":
        ni, mi = map(int, s)
        if num + ni > l:
            print("FULL")
            exit()
        stack.append([ni, mi])
        num += ni

    elif querry == "Pop":
        ni = int(s[0])
        if num - ni < 0:
            print("EMPTY")
            exit()
        num -= ni
        while ni > 0:
            nj, mj = stack.pop()
            if nj <= ni:
                ni -= nj
            else:
                nj -= ni
                stack.append([nj, mj])
                ni = 0

    elif querry == "Top":
        if num == 0:
            print("EMPTY")
            exit()
        else:
            print(stack[-1][1])

    else:
        print(num)
else:
    print("SAFE")
