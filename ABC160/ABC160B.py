a=int(input())
result=a//500*1000
a=a%500
result+=a//5*5
print(result)