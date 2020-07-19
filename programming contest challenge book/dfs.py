n = 4
a = (1, 2, 4, 7)
k = 13

# n = int(input())
# a = [int(i) for i in input().split()]
# k = int(input())

num_list = []
has_ans = False
ans_list = []
def dfs(i, j):
    global num_list
    global has_ans
    global ans_list
    if i == n and j == 1:
        num_list.append(a[i-1])
        sum_num = sum(num_list)
        # num_list = []
        print(sum_num)
        return sum_num
    elif i == n and j == 0:
        sum_num = sum(num_list)
        print(sum_num)
        return sum_num
    # if j == 0　:
    #     return 0
    if j == 1:
        num_list.append(a[i-1])
        

    if dfs(i + 1, 0) == k:
        # print("Yes", num_list)
        has_ans = True
        ans_list = num_list[::]
    for delete_num in range(n - i - 1):
        num_list.pop()
    if dfs(i + 1, 1) == k:
        # print("Yes", num_list)
        has_ans = True
        ans_list = num_list[::]

dfs(0, 0)

if has_ans:
    print("Yes", ans_list)
else:
    print("No")