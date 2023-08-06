import operator # for standart operators: operator.itemgetter(1)

import pprint  #pretyprint of dictionaries

import json # also prettyprint and dump

#test disassembler
import dis


name_for_userid = {
    382 : 'Alice',
    950 : 'Bob',
    590 : 'Dilbert'
}

def greeting_except(userid):
    '''get value from Dict with exception'''
    try:
        return 'Hi %s!' % name_for_userid[userid]
    except KeyError:
        return 'Hi there'

def greeting(userid):
    '''get value from Dict with get method'''
    return 'Hi %s!' % name_for_userid.get(userid, 'there')  #.get(key, defaultvalue if not found)


def handle_a(x,y):
    return 'a: ' + str(x+y)

def handle_b(x,y):
    return 'b: ' + str(x-y)

def handle_default():
    return 'Nop operation'

#all in one function
def dispatch_dict(operator, x,y):
    return {
        'add' : lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(operator, lambda : None)()

def test_Dict_tricks():
    print('Testing Dict tricks')

    print(greeting_except(950))
    print(greeting_except(333333)) # no Key in Dict

    print(greeting(382))
    print(greeting(333333))  # no Key in Dict

    print('Sorting dict..')
    xs = {'a':4, 'c':2, 'b':3, 'd':1}
    print(sorted(xs.items()))

    print('Sorting dict with lambda..')
    print(sorted(xs.items(), key=lambda x: x[1])    )

    print('Sorting dict with standart Operator..')
    print(sorted(xs.items(), key=operator.itemgetter(1))  )

    print('Sorting dict in Reverse order..')
    print(sorted(xs.items(),
                 key=lambda x: x[1],
                 reverse=True) )

    print('\nEmulate Switch/Case statements:')
    func_dict = {
        'cond_a' : handle_a,
        'cond_b': handle_b,
    }
    result_A = func_dict.get('cond_a', handle_default)(10, 5)
    print(result_A)
    result_B = func_dict.get('cond_b', handle_default)(5,10)
    print(result_B)
    print(func_dict.get('Wrong_code', handle_default)())

    print('\n Function dispatch_dict')
    print(dispatch_dict('mul', 2,8))
    print(dispatch_dict('div', 0, 1))
    print(dispatch_dict('unknown', 2, 8))

    print('\n Merge Dictitonaries..')
    xs = {'a': 1, 'b': 2}
    ys = {'b': 3, 'c': 4}

    zs = { }
    zs.update(xs)
    zs.update(ys)
    for key, value in zs.items():
        print(f'key={key}' f'  value={value}')

    print('Merge with zs = {**xs, **ys}')
    ws = {'d': 2, 'c': 6}
    new_zs = {**xs, **ys, **ws }

    for key, value in new_zs.items():
        print(f'key:{key}' f'  value:{value}')

    print('\nPretty-Print:')
    mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee, 'd' : set([1,2,3])}
    pprint.pprint(mapping)

    print('\nPretty-Print and dump Json:')
    mapping = {'a' : 23, 'b':42, 'c' : 0xc0ffee}
    dump_result = json.dumps(mapping, indent=4, sort_keys=True)
    print(dump_result)

    print('\nDisassemble the function:')
    print(dis.dis(handle_a))
