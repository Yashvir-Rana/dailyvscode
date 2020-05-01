# the lambda function
def m_i(n):
    return  lambda x: x+n

f = m_i(41)
print(f(0))
print(f(1))
