"""
you want to implement a custom iteration pattern thats
different than the usal built in function (range(), reversed(), etc)
"""
# own iterate function
def frange(start, stop, increment):
    """generator that produce a range of floating pt. no."""

    x = start
    while x < stop:
        yield x
        x += increment

for n in frange(0, 4, 0.5):
    print(n)

# the presence of yield staement in function makes in generator,
# a generator only in response to iteration.

def countdown(n):
    print('start to count from...', n)
    while n > 0:
        yield n
        n -= 1
    print('done')

c = countdown(5)
print(c)
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))