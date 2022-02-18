s = input()
zero = 0
one = 0

for i in s:
    if i == "0":
        zero += 1
    else:
        one += 1
        
res = min(zero, one) * 2
print(res) 