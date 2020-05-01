# joining string

def concatenation(*args, sep = '/'):
    return sep.join(args)
print(concatenation("A", "B", "C", sep=","))