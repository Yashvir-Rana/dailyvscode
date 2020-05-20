""""
you need to unpack N element from an 
iterable, but the iterable may be longer than N elements,
causing a "too amnty value to unpack" exception.
"""
def drop_first_last(grades):
    first, *middle, last = grades
    return (middle)

grades = (40, 55, 55, 55, 42)
print(drop_first_last(grades))
# demo
record = ('dave', 'davdbh@gmail.co', '555562496', '5641546123')
name, email, *phone = record
print(phone)

sales = [10, 9, 3, 5, 6, 5, 7, 1]
*trailing_qtr, current_qtr = sales
trailing_avg = sum(trailing_qtr) / len(trailing_qtr)
print(current_qtr)
print(trailing_avg)

rec = [('foo', 1, 2), ('bar', 'hello'), ('foo', 3, 4),]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in rec:
    if tag == 'foo':
        do_foo(*args)
    else:
        do_bar(*args)

# string processing with star

line = "nobody:*:-2:-2:unpre user:/var/empty:/user/bin/True"
uname, *fields, homdir, sh = line.split(':')
print(uname)
print(fields)
print(homdir)
print(sh)

# to ignore

re = ('acme', 50, 123, 42, (12, 5, 2020))
name, *_, (*_, year) = re
print(year)

