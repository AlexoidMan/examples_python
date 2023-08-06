import copy

def copy_testing():

    xs = [ [1,2,3], [4,5,6], [7,8,9] ]
    ys = list(xs)  #shallow copy
    ys_2 = xs  # reference to xs obj
    ys_3 = copy.copy(xs)

    print(xs)
    print(ys)
    print(ys_2)
    print(ys_3)

    xs.append([999, 888, 666])

    print(f' After modify')
    print(xs)
    print(ys)
    print(ys_2)
    print(ys_3)

    print(f' Deep copy')
    xs = [ [1,2,3], [4,5,6], [7,8,9] ]
    ys = copy.deepcopy(xs)  # deep copy
    xs[1][0] = 'New Value'
    print(xs)
    print(ys)

    return None