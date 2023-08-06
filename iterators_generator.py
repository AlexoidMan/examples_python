

class Repeater:
    '''repeater class with infitine iteration '''
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        return self.value


class BoundedRepeater:
    def __init__(self, value, max_iterations):
        self.value = value
        self.maxIter = max_iterations
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if(self.count >= self.maxIter):
            raise StopIteration

        self.count += 1
        return self.value + '_' + str(self.count)


def repeaterGen(value):
    '''generator'''
    while True:
        yield value
        print("      value Yielded...")

def repeateGen_3times(value):
    '''generator'''
    yield value
    print("    1  value Yielded...")
    yield value
    print("    2  value Yielded...")
    yield value
    print("    3  value Yielded...")

def bounded_repeaterGen(value, max_repeats):
    ''' generator , limited to max_repeats '''
    for i in range(max_repeats):
        yield value


### Iterator Chains :
def integers():
    for i in range(1,9):
        yield i   # generator

def squared(seq):
    for i in seq:
        yield i * i

def negative(seq):
    for i in seq:
        yield -i


###

def test_iterators():
    ''' Simple Iterable class'''

    repeater = Repeater('Hey')

    print(next(repeater))
    print(next(repeater))
    print(next(repeater))


    bounded_repeater = BoundedRepeater('Hey Dude!', 5)

    for item in bounded_repeater:
        print(item)

  ### Generator analog to classes Repeater, Bounded Repeater
    # for x in repeaterGen('Hi'):
    #     print(x)

    for x in repeateGen_3times('Hi'):
         print(x)

    for x in bounded_repeaterGen('Hi bounded', 4):
         print(x)


    ## Generator expressions
    print('Generator expressions: genexpr = (expression for item in collection if condition)')
    print('Generator expressions: (\'Hello\' for i in range(3)\)')
    iterator_genExpr = ('Hello' for i in range(3))

    for x in iterator_genExpr:
        print(x)

    #convert generator expression into list (GE can be iterated ONLY ONCE)
    print('convert GE into List')
    iterator_genExpr_convert = ('GE into List' for i in range(3))
    list_from_ge = list(iterator_genExpr_convert)
    for x in list_from_ge:
        print(x)

    iterator_genExpr_convert = ('Hey_' + str(i) for i in range(3))
    print(next(iterator_genExpr_convert))
    print(next(iterator_genExpr_convert))
    print(next(iterator_genExpr_convert))
    # print(next(iterator_genExpr_convert)) fails - exceeds iterator boundaries

    #filtering values
    print('Filter values in ge')
    squaresfilter_iterator = ( x*x for x in range(10) if x%2 == 1)   # [0..9]
    for x in squaresfilter_iterator:
        print(x)

    #In-line Generator Expressions
    print('In-line Generator Expressions')
    for x in ('Bom dia' for i in range(3)):
        print(x)

    sum1020 = sum(x*2 for x in range(10,20) )
    print(f'Sum of 2*([10-20]): ' f'{sum1020}')

    # iterator chains
    print('Iterator chains:   chain = negative(squared(integers()))')
    chain = negative(squared(integers()))
    listFromChain = list(chain)
    for x in listFromChain:
        print(x)