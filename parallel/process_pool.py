import multiprocessing
import time

## Run 12 tasks in only 4 processes using Pool

def function(i):
    process = multiprocessing.current_process()
    print("start Task %i(pid:%s)" %(i, process.pid))
    time.sleep(2)
    print("end Task %i(pid:%s)" %(i, process.pid))
    return

if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=3)

    print("Processes started: %s" %(pool._processes))

    ## create 12 tasks in 3 Processes
    for i in range(12):
        results = pool.apply(function, args=(i,))

    pool.close()

    print("END Program")