"""you want to make a list of the largest or smallest N
    items in acollection"""
"""sol: the heapq module has two functions nlargest() and nsmallest()
        that do exactly what you want."""

import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

portfolio = [
        {'name': 'ibm', 'shares': 100, 'price': 91.1},
        {'name': 'aapl', 'shares': 50, 'price': 543.22},
        {'name': 'fb', 'shares': 200, 'price': 21.09},
        {'name': 'hp', 'shares': 35, 'price': 31.75},
        {'name': 'yho', 'shares': 45, 'price': 16.35},
        {'name': 'acme', 'shares': 75, 'price': 115.65}
        ]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])

print(cheap)
print(expensive)