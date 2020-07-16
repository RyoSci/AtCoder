n = 4
a = (1, 2, 4, 7)
k = 13

# n = int(input())
# a = [int(i) for i in input().split()]
# k = int(input())

num_list = []
def dfs(i, j):
    global num_list
    if i == n:
        return 0
    # if j == 0:
    #     return 0
    elif j == 1:
        num_list.append(a[i])
        return a[i]

    if dfs(i + 1, 0) + dfs(i + 1, 1) == k:
        print("Yes")

dfs(0, 0)