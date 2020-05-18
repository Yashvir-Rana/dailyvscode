"""
problem: you have an N element tuple
or sequence that you would like to 
unpack into a collection of N variables.
"""

tup = ('aam', 'tarbuj', 'kela')
mango, watermelon, banana = tup 
print(mango, watermelon, banana)

data = ['acme', 50, 52.2, ("2020/5/18")]
name, share, price, date = data
print(date)

s = 'hello'
a, b, c, d, e = s
print(a)

data = ['acme', 50, 52.2, ("2020/5/18")]
_, shares, price, _ = data
print('shares:',shares,'price:',price)

