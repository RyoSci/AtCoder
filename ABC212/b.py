x = input()

if len(set(x)) == 1:
    ans = "Weak"
else:
    cnt = 0
    for i in range(3):
        if (int(x[i])+1) % 10 == int(x[i+1]):
            cnt += 1
    if cnt == 3:
        ans = "Weak"
    else:
        ans = "Strong"
print(ans)
