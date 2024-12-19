import math
import os
import time
import numpy as np
from multiprocessing.pool import Pool

def func(value):
    pid = os.getpid()
    result = math.sqrt(value)
    print("[Pid:%s] The value %s and the elaboration is %s" %(pid, value, result))
    time.sleep(value)
    return result

# if __name__ == '__main__':
#     with Pool() as pool:
#         data = np.array([10, 3, 6, 1, 4, 5, 2, 9, 7, 3, 4, 6])
#         ## map portion=4 elements of data array to 1 process. 4 calls of func() to each process
#         results = pool.map(func, data, chunksize=4)
#         print("The main process is going on...")
#         for result in results:
#             print("This is the result: %s" %result)
#
#     print("END Program")

if __name__ == '__main__':
    with Pool() as pool:
        data = np.array([10, 3, 6, 1, 4, 5, 2, 9, 7, 3, 4, 6])
        ## map portion=4 elements of data array to 1 process. 4 calls of func() to each process
        ## Asynchronously
        results = pool.map_async(func, data, chunksize=4)
        print("The main process is going on...")
        for result in results.get():
            print("This is the result: %s" %result)

    print("END Program")