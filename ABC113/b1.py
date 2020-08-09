"""
半ば強引に二分探査で書いた。
今回の制約は小さかったので、計算量が問題なかったが減らそうと思ったらこのコードも強引だがあり。
"""
#入力
n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))
h_not_sorted = h
h = sorted(h)
x = abs((t - a) / 0.006)

#二分探査
l = 0
r = n - 1
x_index = 0
while l + 1 != r :
    middle = (l + r) // 2
    if h[middle] == x:
        x_index = middle
        break
    elif h[middle] < x:
        x_index = middle + 1
        l = middle
    else:
        x_index = middle - 1
        r = middle


#x_indexが両橋の場合とそれ以外で場合わけ。
res = abs(a - (t - 0.006 * h[x_index]))
ans = x_index
flag_r = True 
flag_l = True
if x_index == n - 1:
    flag_r = False
elif x_index == 0:
    flag_l = False
else:
    pass

#x_indexの両橋と比較。x_indexが際数値でない可能性があるため。
if flag_r:
    if abs(a - (t - 0.006 * h[x_index + 1])) < res:
        res = abs(a - (t - 0.006 * h[x_index + 1]))
        ans += 1
if flag_l:
    if abs(a - (t - 0.006 * h[x_index - 1])) < res:
        res = abs(a - (t - 0.006 * h[x_index - 1]))
        ans -= 1

print(h_not_sorted.index(h[ans]) + 1)