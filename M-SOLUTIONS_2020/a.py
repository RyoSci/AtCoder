x = int(input())
res = 0
if 400 <= x < 600:
    res = 8
elif 600 <= x < 800:
    res = 7
elif 800 <= x < 1000:
    res = 6
elif 1000 <= x < 1200:
    res = 5  
elif 1200 <= x < 1400:
    res = 4 
elif 1400 <= x < 1600:
    res = 3
elif 1600 <= x < 1800:
    res = 2
else:
    res = 1

print(res)    