s = input()
weather = ["Sunny", "Cloudy", "Rainy"]

index = weather.index(s)
index = (index + 1) % 3

print(weather[index])