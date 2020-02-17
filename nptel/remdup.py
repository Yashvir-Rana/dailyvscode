"""def remdup(l):
    new_l = []
    for ele in l:
        if ele not in new_l:
            new_l.append(ele)
    return new_l



l=[7, 3, -1, -5, -5]
print(remdup(l))"""
#############################################################

def remdup(l):
    return set([x for x in l if l.count(x) > 1])

l = [7, 3, 1, -5 , 3]
print(remdup(l))