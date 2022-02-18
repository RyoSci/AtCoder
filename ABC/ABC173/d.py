n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)

min_comfort = max(a)
sum_comfort = max(a)
i = 0
j = 1
counter=0
while i < n - 2:
    tmp = a[j]
    sum_comfort += tmp
    counter+=1
    if counter ==2:
        counter=0
        j+=1
    i+=1
    # print(i,j)
print(sum_comfort)