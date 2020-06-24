satu,money=[int(i) for i in input().split()]
# rest_money=money
# ten=money//10000
# rest_money%=10000
# five=rest_money//5000
# rest_money%=5000
# one=rest_money//1000
# rest_money%=1000

rest_money=money
moneys=[10000,5000,1000]
num_moneys=[0,0,0]
for i in range(3):
    num_moneys[i]=rest_money//moneys[i]
    rest_money=rest_money%moneys[i]

sum_paper_money=ten+five+one
flag=False
if sum_paper_money>satu:
    flag=False
elif sum_paper_money==satu:
    flag=True

rest_paper=satu-sum_paper_money

ten-=rest_paper//9
one+=(rest_paper//9)*10
sum_paper_money=ten+five+one
rest_paper=satu-sum_paper_money
# if rest_paper==0 :
#     # print(ten,five,one)
#     flag=True

five-=rest_paper//4
one+=rest_paper//4*5
sum_paper_money=ten+five+one
rest_paper=satu-sum_paper_money
# if rest_paper==0:
#     # print(ten,five,one)
#     flag=True

ten-=rest_paper
five+=rest_paper*2
sum_paper_money=ten+five+one
rest_paper=satu-sum_paper_money
if rest_paper==0:
    # print(ten,five,one)
    flag=True

if flag and ten>=0 and five>=0 and one>=0:
    print(ten,five,one)
else:
    print(-1,-1,-1)

# satu,money=[int(i) for i in input().split()]
# rest_money=money
# ten=money//10000
# rest_money%=10000
# five=rest_money//5000
# rest_money%=5000
# one=rest_money//1000
# rest_money%=1000

# sum_paper_money=ten+five+one
# flag=False
# if sum_paper_money>satu:
#     # print(-1,-1,-1)
#     flag=False
# elif sum_paper_money==satu:
#     # print(ten,five,one)
#     flag=True

# rest_paper=satu-sum_paper_money
# if rest_paper!=0 and rest_paper//9<=ten:
#     ten-=rest_paper//9
#     one+=(rest_paper//9)*10
#     sum_paper_money=ten+five+one
#     rest_paper=satu-sum_paper_money
#     if rest_paper==0 :
#     	# print(ten,five,one)
#         flag=True
# if rest_paper!=0 and rest_paper//4<=five:
#     five-=rest_paper//4
#     one+=rest_paper//4*5
#     sum_paper_money=ten+five+one
#     rest_paper=satu-sum_paper_money
#     if rest_paper==0:
#         # print(ten,five,one)
#         flag=True
# if  rest_paper!=0 and rest_paper<ten:
#     ten-=rest_paper
#     five+=rest_paper*2
#     sum_paper_money=ten+five+one
#     rest_paper=satu-sum_paper_money
#     if rest_paper==0:
#         # print(ten,five,one)
#         flag=True

# if flag and ten>=0 and five>=0 and one>=0:
#     print(ten,five,one)
# else:
#     print(-1,-1,-1)
