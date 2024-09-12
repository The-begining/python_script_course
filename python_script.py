#decorators 
def uppercase_decorator(function):
    def inner():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return inner
    
def say_hello():
    return "hello there!"

#deco = uppercase_decorator(say_hello)
#print(deco())

@uppercase_decorator
def say_hello():
    return "Hello there !"

print(say_hello())