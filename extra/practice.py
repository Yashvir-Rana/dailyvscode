# import random

# message = ['yoman1',
#         'koman3',
#         'choman4',
#        ]
# print(message[random.randint(0,len(message)-1)])

# import copy

# a = [1,2,3,4]
# b = copy.copy(a)
# b.append(5)
# print(a, b)

# c
# dictionaries methods:

# a = {'a':'123', 'b':'apu'}
# print(a.keys()) # show keys of the dict.
# print(a.values()) # show corresponding values of keys
# a.items() # show both in a tuple.
# print('list:',list(a.items())) # convert tuple into list

# for k,v in a.items():
# print('keys:',k,'--->' 'value:', v )
# -----------------------------------------------------------------

# picnicitem = {'apple': 5, 'banana': 12, 'kiwi': 6}

# while True:
#  print('enter key:')
#  key = input()
#  print('the no. of fruits is ' + str(picnicitem.get(key , 0)), key)
# ---------------------------------------------------------------------
# using setdefaul()
# spam = {'name': 'pupu', 'age': 5}
# spam.setdefault('class', 'kg')
# print(spam)
# ---------------------------------------------------------------------
# using setdefault(key,value) to  counts the number of occurrences of each letter in a string

# message = 'i am born intelligent, and i am confident.'
# count = {}

# for character in message:
# count.setdefault(character, 0)
# count[character] = count[character] + 1

# print(count)
# ---------------------------------------------------------------------------
# using pprint()
# import pprint

# message = 'i am born intelligent, and i am confident.'
# count = {}

# for character in message:
# count.setdefault(character, 0)
# count[character] = count[character] + 1

# pprint.pprint(count)
# --------------------------------------------------------------------------------

"""print('hello world?')
print("what is your name?")
my_name = input()
print("your name is ", my_name)
print("length of you name is:", len(my_name))
print('what is your age')
my_age = input()
print("your age will be ", str(int(my_age) + 1), " in a year")"""


# ----------------------------------------------------------------------------------
# define a function greatest common divisor
#def gcd(m, n):
    # collecting factors of m
#    fm = []
#    for i in range(1, m + 1):
 #       if m % i == 0:
  #          fm.append(i)
   # print('factor of m:', fm)
    # collecting factors of n
    #fn = []
    ##for j in range(1, n + 1):
      #  if n % j == 0:
       #     fn.append(j)
    #print('factor of n:', fn)
    # compare factors and return the highest factor
    #cf = []
    #for f in fm:
     #   if f in fn:
      #      cf.append(f)
    #return print('the common factor is:', cf[-1])

#gcd(62,20)

""" def gcd(m, n):
        cf = []
        for i in range(1,min(m,n)+1):
            if m%i == 0 and n %i == 0 :
                cf.append(i)
    return print(cf[-1])
 gcd(16, 20)"""

"""def gcd(m, n):
    for i in range (1, min(m,n) +1):
        if m%i == 0 and n%i == 0:
            recentcf = i
    return print(recentcf)
gcd(16, 20)"""
# ---------------------------------------------------------
"""x = [423, 'b', 37, 'f']
u = x[1:]
y = u
w = x
u = u[0:]
u[1] = 53
x[2] = 47
print(x,y,u,w )"""
# ----------------------------
"""first  = "tarantula"
second = ""
for i in range (len(first)-1,-1,-1):
    second = first[i] + second
print(second)"""
#------------------------------------
"""def mystery(l):
    l = l[0:5]
    return ()
list1 = [44, 71, 12, 8, 23, 17, 16]
mystery(list1)
print(list1)"""

