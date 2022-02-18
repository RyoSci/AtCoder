n = input()
for i in range(3):
    if n[i + 1] == n[i]:
        pass
    else:
        print("DIFFERENT")
        break
else:
    print("SAME")
