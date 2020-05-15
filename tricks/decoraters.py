# decorators are increse or modify the behaiour of a function.
# decorators alow you to extend and modify the behaiour of a callable(function, method, class)
# without permanently modifying the callable itself.


def deco(func):
    def inner(a, b):
        if a < b :
            a, b = b, a
        return func(a, b)
    return inner

@deco
def div(a, b):
    print(a/b)
    
div(1, 2)