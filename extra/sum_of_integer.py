i =int(input("enter any three digit no."))
a = list(map(int, i))
print(a)
x = a[0]*i
print(x)
y = a[1]*(i%100 - 3)
z = a[2]*(i%10 -3)
print(x+y+z)