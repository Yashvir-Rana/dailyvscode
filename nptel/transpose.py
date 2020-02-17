def transpose(m):
    tr = list(map(list, zip(*m)))
    return tr

m = [[1,2,3],[4,5,6]]
print(transpose(m))
