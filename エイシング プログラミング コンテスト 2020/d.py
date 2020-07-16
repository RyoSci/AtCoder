import math
# print(math.log(2*10**5))

n = int(input())
x = input()
z = 0
exp_2 = [0] * (2 * 10**5 + 1)
exp_2[0] = 2**n
for i in range(1, n + 1):
    exp_2[i] = exp_2[i - 1]// 2
    z += exp_2[i]*int(x[i - 1])
num_1 = x.count("1")
list_num_1 = [0] * (2*10**5+1)
# list_num_1[0] = 0
index = 0
for i in range(1, 2*10**5+1):
    # if math.log2(i).is_integer():
    #     list_num_1[i] = int(math.log2(i)) 
    # else:
    #     list_num_1[i] = int(math.log2(i)) + 1
    if math.log2(i).is_integer():
        index = 0
    list_num_1[i] = list_num_1[index] + 1
    index += 1
print(list_num_1[0:10])
for i in range(n):
    if x[i] == "0":
        tmp_num_1 = num_1 + 1
        tmp_z = exp_2[i + 1] + z #modify ok
    elif x[i] == "1":
        tmp_num_1 = num_1 - 1
        tmp_z = -exp_2[i + 1] + z #modify ok
    counter = 0
    while tmp_z > 0:
        tmp_z = tmp_z % tmp_num_1
        tmp_num_1 = list_num_1[tmp_z] #modify
        counter += 1
    print(counter)
