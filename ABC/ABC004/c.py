n = int(input())
cards = ""
n %= 30
l = n // 5 + 1
for i in range(6):
    tmp = l % 6
    if tmp == 0:
        tmp = 6
    cards += str(tmp)
    l += 1

index = n % 5
insert_num = cards[0]
cards = list(cards[1:])
cards.insert(index, insert_num)
print("".join(cards))
