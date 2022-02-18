n , d = map(int, input().split())
can_see_num = 2*d + 1
print((n + can_see_num - 1) // (can_see_num))