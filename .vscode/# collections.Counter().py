# collections.Counter()

# problem statement:
#"""Ram is a shoe shop owner. His shop has X number of shoes.
#He has a list containing the size of each shoe he has in his shop.
#There are N number of customers who are willing to pay x1 amount of money 
# only if they get the shoe of their desired size.
#Your task is to compute how much money Ram earned."""

from collections import Counter

X = int(input())
shoes = Counter(map(int, input().split()))
N = int(input())
income = 0
for i in range(N):
    size, price = map(int, input().split())
    if shoes[size]:
        income +=  price
        shoes[size] -= 1

print(income)