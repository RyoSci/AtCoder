s = input()
keyence = "keyence"
break_time = 0

j = 0
is_ok_ng = False
for i in s:
    if j < 7 and i == keyence[j]:
        j += 1
        is_ok_ng = True

    else:
        if is_ok_ng:
            break_time += 1
        is_ok_ng = False
        if i > 7 and

    if break_time > 1:
        print("NO")
        break
else:
    if j == 7:
        print("YES")
    else:
        print("No")
