n  = int(input())
a_to_e =[0] * 5
lowest_ride = 10 ** 15 + 1
for i in range(5):
    a_to_e[i] = int(input())
    if a_to_e[i] < lowest_ride:
        lowest_ride = a_to_e[i]

print((n + lowest_ride - 1) // lowest_ride + 4)
