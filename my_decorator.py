
import functools

def strong(func):
    def wrapper():
        return "<strong>" + func() + "</strong>"

    return wrapper


def emphasize(func):
    def wrapper():
        return "<em>" + func() + "</em>"

    return wrapper

def make_upper(func):
    def wrapper():
        return  str.upper(func())

    return wrapper

@strong
@make_upper
@emphasize
def greet():
    return "Hello!"


def greet_pure():
    return "Hello!"
####################################################################
def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Trace: calling {func.__name__}()'
              f'with {args}, {kwargs}')
        original_result = func(*args, **kwargs)

        print(f'Trace: calling {func.__name__}()'
              f'returned {original_result!r}')
        return original_result

    return wrapper

@trace
def say(name, line):
    ''' Function say - is a good way to communicate!!! '''
    return f'{name}: {line}'

###################################################################