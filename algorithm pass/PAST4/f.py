n, k = map(int, input().split())
s_dict = dict()
for i in range(n):
    s = input()
    if s not in s_dict:
        s_dict[s] = 1
    else:
        s_dict[s] += 1

nums = sorted(list(s_dict.values()), reverse=True)
ans_num = nums[k - 1]
if nums.count(ans_num) == 1:
    for key, value in s_dict.items():
        if value == ans_num:
            print(key)
            break
else:
    print("AMBIGUOUS")
