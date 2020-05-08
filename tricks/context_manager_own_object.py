# supporting with your own objecct:
# by creating context managers- it's a simple "protocol"
# or interface that your object need to follow in order to support with statement.
# all you need to do is:
# add __enter__ and __exit__ method to an object

class managedfile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file  = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, exc_tb):
        if self.file:
            self.file.close()

with managedfile('hello.txt') as f:
    f.write('hello, world!')
    f.write('\nbye, now')