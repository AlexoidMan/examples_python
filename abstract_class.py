from abc import ABCMeta, abstractmethod

class BaseSimple:

    def foo(self):
        raise NotImplementedError()

    def bar(self):
        raise NotImplementedError()

class ConcreteSimpe(BaseSimple):
    def foo(self):
        return 'foo() called'


class Base( metaclass=ABCMeta ):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass

class Concrete(Base):
    def foo(self):
        return 'foo() called'

    def bar(self):
        return 'bar() called'



def test_abstract():
    # b = ConcreteSimple()
    # print(b.foo())
    # print(b.bar())

    assert issubclass(Concrete, Base)
    b = Concrete()
    print(b.foo())
    print(b.bar())

