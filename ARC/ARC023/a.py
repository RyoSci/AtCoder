y, m, d = [int(input()) for i in range(3)]

def cal(y, m, d):
    if m == 1 or m == 2:
        m += 12
        y -= 1

    return 365 * y + int(y / 4) - int(y / 100) + int(y / 400) + int(306 * (m + 1) / 10) + d - 429
    
print(cal(2014, 5, 17) - cal(y, m, d))
