# decorators are increse or modify the behaiour of a function.
# decorators alow you to extend and modify the behaiour of a callable(function, method, class)
# without permanently modifying the callable itself.


def deco(func): # decorator
    """this is a decorator"""
    def inner(a, b): # closure
        if a < b :
            a, b = b, a
        return func(a, b)
    return inner
"""
def div(a, b):
    print(a/b)
div1 = deco(div)
div1(1, 2)
"""
@deco
def div(a, b):
    print(a/b)

div(1, 2)
print(deco.__doc__) # docstring 