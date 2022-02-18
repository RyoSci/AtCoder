n = int(input())
s = n % 60
m = n // 60
h = m // 60
print(str(h).zfill(2) + ":" + str(m % 60).zfill(2) + ":" + str(s).zfill(2))
