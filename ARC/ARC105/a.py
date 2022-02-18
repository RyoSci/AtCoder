abcd = list(map(int, input().split()))
abcd.sort()
if abcd[-1] == sum(abcd[:3]) or abcd[-1] + abcd[0] == abcd[1] + abcd[2]:
    print("Yes")
else:
    print("No")
