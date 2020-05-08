# with statement simplify common resource manangement
# build-in open() provide excellent case.
# 1. open file descriptor automatically closed after program exectuion leaves.
with open('hello.txt', 'w') as f :
    f.write('heloo, world1!')
# behind the scene
"""
f = open('hello.txt', 'w')
try:
    f.write('hello, world!')
finally:
    f.close()

"""
# 2. threading.lock()

some_lock = threading.lock()
# harmful:
try:
    # do something...
finally:
    some_lock.release()

# better:
with some_lock :
    # do something...

