x = input()

ans = "Strong"

if len(set(x)) == 1:
    ans = "Weak"

for i in range(3):
    if (int(x[i])+1) % 10 == int(x[i+1]):
        continue
    else:
        break
else:
    ans = "Weak"

print(ans)
