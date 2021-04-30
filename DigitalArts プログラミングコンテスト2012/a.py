s = input().split()

n = int(input())
t = [input() for _ in range(n)]

ans = []
for si in s:
    is_break = False
    for j in range(n):
        if len(si) != len(t[j]):
            continue
        else:
            for k in range(len(si)):
                if t[j][k] == "*" or si[k] == t[j][k]:
                    continue
                else:
                    break
            else:
                ans.append("*" * len(si))
                is_break = True
        if is_break:
            break
    else:
        ans.append(si)

print(*ans)
