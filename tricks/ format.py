n = 'yash'
print("the name is %s"%n) # old style
print("the name is %(n)s"%{'n':n}) # old style
print("the name is", n.format()) # new style
print(f"the name is {n}") # python 3.6 above
