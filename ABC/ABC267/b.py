# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

s = input()
retu = [0]*7
num2retu = [3, 2, 4, 1, 3, 5, 0, 2, 4, 6]
for i in range(10):
    if s[i] == "1":
        retu[num2retu[i]] += 1

if s[0] == "0":
    ans = "No"
    for i in range(7):
        if retu[i] == 0:
            flag0 = False
            flag1 = False
            for j in range(i):
                if retu[j] > 0:
                    flag0 = True
            for j in range(i, 7):
                if retu[j] > 0:
                    flag1 = True
            if flag0 and flag1:
                ans = "Yes"
                break
    print(ans)
else:
    print("No")
