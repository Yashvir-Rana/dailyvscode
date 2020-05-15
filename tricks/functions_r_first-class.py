#function are object

def yell(text):
    return text.upper() + '!'

print(yell('hello'))
bark = yell
print(bark('woof'))
try :
    del yell
    print(yell('hello'))
except:
    print(bark('woo'))
print(bark.__name__)


#functions can be stored in data structure

function = [bark, str.lower, str.capitalize]
print(function)
for f in function:
    print(f, f('hey there'))
print(function[0]('heyho'))

# function can be passed to other function
# higher order function

def greet(fun):
    greeting =fun('hey its yash')
    print(greeting)
print(greet(bark))
def whisper(text):
    return text.lower() + '......'
print(greet(whisper))

# classical eg is map function

print(list(map(bark, ['hey', 'hi', 'hello'])))

