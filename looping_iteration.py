



def test_loop_iteration():
    print(f' Writing Pythonic Loop:')

    my_items = ['a','b','c', 'd']

    for i in range(len(my_items)):
        print(my_items[i])

    print("as for-each:")
    for item in my_items:
        print(item)

    print("if you need index - use enumerate")
    for i, item in enumerate(my_items):
        print(f'{i}: {item}')

    emails = {'bob': 'bob@example.com',
              'alice': 'alice@example.com',}
    print("Dictionary, print keys/values - use emails.items()")
    for name, email in enumerate(emails.items()):
        print(f'{name}: {email}')


    print("if you need index and step in Loop - use range(a,n,s)")
    a = 0 # start value
    n = len(my_items) # stop value
    s = 2 # step
    for i in range(a, n, s):
        print(f'{i}: {my_items[i]}')

def test_comprehensions():
    print("List comprehension: [expression for item in collection]")
    squares = [ x * x for x in range(10)]
    print(squares)

    print("List comprehension: if condition")
    even_squares = [x * x for x in range(10) if x % 2 == 0 ]
    print(even_squares)

    print("Set comprehension:")
    set_values = {x * x for x in range(-9, 10)}
    print(set_values)

    print("Set comprehension:")
    dict_values = { 'o' + str(x) : x * x for x in range(10)}
    print(dict_values)

def test_list_slicing():
    print("List slicing: [start, end, stride]")
    lst = [2, 3, 5, 7]

    print(f'lst[:2]  {lst[:2]}')
    print(f'lst[:-2]  {lst[:-2]}')
    print(f'lst[::2]  {lst[::2]}')
    print(f'reverse list lst[::-1]  {lst[::-1]}')
    print(f'lst[-3:]  {lst[-3:]}')
    print(f'lst[-3::-1]  {lst[-3::-1]}') #get last 3 elements and reverse them

    del lst[:]
    # lst.clear()
    print(f'del lst[:]  {lst}')

    lst = [2, 3, 5, 7]
    copied_lst = lst[:]
    print(f'create shallow copies  {copied_lst}')

