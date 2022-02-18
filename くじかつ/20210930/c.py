import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, a, b, c, d = map(int, input().split())
s = input().strip()

if c < d:
    i = b-1
    while 1:
        if i == d-1:
            break
        if s[i+1] == ".":
            i += 1
        elif s[i+2] == ".":
            i += 2
        else:
            i = -1
            break
    j = a-1
    while 1:
        if j == c-1:
            break
        if s[j+1] == "." and j+1 != i:
            j += 1
        elif s[j+2] == "." and j+2 != i:
            j += 2
        else:
            j = -1
            break
    if i == d-1 and j == c-1:
        ans = "Yes"
    else:
        ans = "No"
else:
    i = b-1
    j = a-1
    while 1:
        flag1 = True
        flag2 = True

        # 行けるだけいく
        # 進まなかったらflagはFalse
        while 1:
            if j == c-1:
                flag1 = False
                break
            elif s[j+1] == "." and j+1 != i:
                j += 1
            elif s[j+2] == "." and j+2 != i:
                j += 2
            else:
                flag1 = False
                break

        # 進まなかったらflagはFalse
        if i == d-1:
            flag2 = False
        elif s[i+1] == "." and i+1 != j:
            i += 1
        elif s[i+2] == "." and i+2 != j:
            i += 2
        else:
            flag2 = False

        if i == d-1 and j == c-1:
            ans = "Yes"
            break
        elif flag1 == False and flag2 == False:
            ans = "No"
            break


print(ans)
