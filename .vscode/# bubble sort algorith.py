# bubble sort algorith
def bubble_sort(lst):
    for border in range(len(lst)- 1, 0, -1):
        for i in range(border):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst
list_to_sort = [27, 0, 71, 70, 27, 63, 90]
print(bubble_sort(lst= list_to_sort))
