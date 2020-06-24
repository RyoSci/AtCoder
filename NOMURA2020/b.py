# t=input()
# print(t.replace("?","D"))

t = input()
n = len(t)
moji = ""
res = ""
if t[-1] ==  "?":
    moji = "P"
    
for i in range(n-1, 0, -1):
    if t[i] == "?":
        if moji == "D" and t[i -1] == "D":
            res += "P"
        elif moji == "P" or moji == "D" and t[i -1] == "P" :
            res += "D"
        elif moji == "P"  and t[i -1] == "?" :
            res += "D"            
        elif moji == "D"  and t[i -1] == "?" :
            res += "P"
           
    else:
        res += t[i]
    moji = res[-1]
if t[0] ==  "?":
    if moji == "P":
        res += "D"
    else:
        res += "P"
else:
    res += t[0]

res = res[::-1]
print(res)