import array



def test_namedtuple():
    arr_float = array.array('f', (1.0, 2.0, 3.2, 4.1))
    print("Array float: {}".format(arr_float))

    arr_bolean = array.array('b', (False, True, False ))
    print("Array bools: {}".format(arr_bolean))

    string1 = 'absdeg'
    list_string1 = list(string1)
    print(f'{list_string1}')
    list_string1[2] = '55'

    string1_back = ''.join(list_string1)
    print(f'{string1_back}')

    #immutable value 0 - 255
    arr_bytes = bytes((0,2,4,6,8,10))
    print(f'{arr_bytes}')

    # mutable byte array
    arr_bytearray = bytearray((0, 2, 4, 6, 8, 10))
    arr_bytearray[5] = 5
    arr_bytearray.append(42)
    arr_bytearray.append(43)
    print(f'{arr_bytearray}')

    #convert back to bytes
    arr_bytes = bytes(arr_bytearray)
    print(f'{arr_bytes} + "  Size" + {arr_bytes.__sizeof__() } ')
    print(f' {len(arr_bytes)}')