# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
def input(): return sys.stdin.readline().rstrip()


n = int(input())
s = input()

nums = s.split("=")
res = []

for num in nums:
    tmp = 0
    i = num.split("+")
    for j in i:
        tmp += int(j)
    res.append(tmp)

ans = "Yes"
for i in range(len(res)-1):
    if res[i] != res[i+1]:
        ans = "No"

print(ans)
