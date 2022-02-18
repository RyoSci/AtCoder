n = int(input())
s = dict()
s["AC"]=0
s["WA"]=0
s["TLE"]=0
s["RE"]=0

for i in range(n):
    si = input()
    s[si] += 1

a = ["AC", "WA", "TLE", "RE"]
for i in a:
    print(i + " x " + str(s[i]))