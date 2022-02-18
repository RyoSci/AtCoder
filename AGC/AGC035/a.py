from collections import Counter
n = int(input())
a = list(map(int, input().split()))
nums = Counter(a)

ans = "No"
if len(nums) == 1 and 0 in nums:
    ans = "Yes"
elif len(nums) == 2 and 0 in nums:
    x, y = sorted(list(nums.values()))
    if x * 2 == y and nums[0] == x:
        ans = "Yes"
elif len(nums) == 3:
    x, y, z = nums.keys()
    if x ^ y == z and nums[x] == nums[y] == nums[z]:
        ans = "Yes"

print(ans)
