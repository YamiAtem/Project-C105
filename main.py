import math
import pandas


def mean(data):
        n = len(data)
        total = 0
        
        for x in data:
            total += int(x)

        mean = total / n
        return mean


reader = pandas.read_csv("https://raw.githubusercontent.com/whitehatjr/std_deviation/master/data.csv")
data = list(reader)

data_mean = mean(data)

squared_list= []

for number in data:
    number_1 = int(number) - mean(data)
    squared_number = number_1**2
    squared_list.append(squared_number)

sum = 0
for average in squared_list:
    sum = sum + average

result = sum / (len(data)-1)
std_deviation = math.sqrt(result)

print(std_deviation)
