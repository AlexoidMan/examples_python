
''' '''
class Meta(type):
    '''metaclass for creating futher classes. Based on class type'''
    def __new__(cls, name, bases, dct):
        x = super().__new__(cls, name, bases, dct)
        x.attr = 100
        return x

class Foo(metaclass=Meta):
    pass

class Bar(metaclass=Meta):
    pass

def test_metaclasses():
    print('Test metaclasses')
    print(Foo.attr)
    print(Bar.attr)