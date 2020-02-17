"""def sumsquare(l):

    odd_l = []
    even_l = []

    for e in l:
        if e%2 != 0:
            odd_l.append(e*e)
        else:
            even_l.append(e*e)
    return list((sum(odd_l), sum(even_l)))

l=[-1, -2, 3, 7]
print(sumsquare(l))"""

"""def sumsquare(l):
    odd = sum(x * x for x in l if x%2 != 0)
    even = sum(x * x for x in l if x % 2 == 0)
    list = [odd,even]
    return list


l =[-1, -2, 3, 7]
print(sumsquare(l))"""
