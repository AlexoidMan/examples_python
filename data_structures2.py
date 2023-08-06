import queue
from struct import Struct
from types import SimpleNamespace
from collections import Counter
from collections import deque

from queue import LifoQueue, Queue, PriorityQueue
from multiprocessing import Queue as multiprocessing_Queue

import heapq

def test_datastructs():
    MyStruct = Struct('i?f')
    data = MyStruct.pack(23, False, 42.0)
    print("data: {}".format(data))
    data_unpack = MyStruct.unpack(data)
    print("unpack data: {}".format(data_unpack))

    car1 = SimpleNamespace(color = 'red', mileage=3232.4, automatic=True)
    car1.mileage = 222.222
    print("car1(SimpleNameSpace): {}".format(car1))

    #set
    vowels = {'a', 'e', 'i', 'o', 'u'} #set
    squares = {x*x for x in range(10)}  # range(0,9)

    print(f' e Exists? : {"e" in vowels}'  f'\n g Exists? : {"g" in vowels}')
    # print(f'squares set: {sort(squares)}'  f'\n g Exists? : {"g" in vowels}')

    letters = set('alice')
    print(f' letters intersection : {letters.intersection(vowels)}')

    vowels.add('x')
    vowels.add('c')
    print(f' letters intersection : {letters.intersection(vowels)}')

    vowels_frozen = frozenset({'a', 'e', 'i', 'o', 'u'})
    # vowels_frozen.add('x')  error!

    #MultiSets
    inventory = Counter()
    loot = {'sword' : 1,'bread': 3 }
    inventory.update(loot)
    print(f' inventory : {inventory}')

    more_loot = {'sword': 1, 'apple': 1}
    inventory.update(more_loot)
    print(f' inventory + more_loot : {inventory}')

    print(f' inventory : Unique {len(inventory)}'  f' inventory : Total no. elements {sum(inventory.values())}')

    #Stacks
    #1. List -based dynamic array ~ O(1) or O(N)
    s =[]
    s.append('eat')
    s.append('sleep')
    s.append('code')
    s.pop()
    print(f'list-based stack s: {s}')

    #2.collections.deque - Fast&Robust  -Double-Linked List O(1)
    s_deque = deque()
    s_deque.append('eat')
    s_deque.append('sleep')
    s_deque.append('code')
    s_deque.pop()
    s_deque.pop()
    print(f'collections.deque stack s_deque: {s_deque}')
    s_deque.pop()
    # s_deque.pop()

    #3.queue.LifoQueue - Parallel Computing
    queue = LifoQueue()
    queue.put('eat')
    queue.put('sleep')
    queue.put('code')
    print(queue.get()) # code
    print(f'queue.LifoQueue  queue: {queue}')
    print(queue.get())# sleep
    print(queue.get()) # eat
    # queue.get() # Blocks / waits forever ...


    #4.Queue (collections.deque) - Fast&Robust  -Double-Linked List O(1)
    # FIFO
    deque_fifo = deque()
    deque_fifo.append('eat')
    deque_fifo.append('sleep')
    deque_fifo.append('code')
    print(f'collections.deque Queue FIFO: {deque_fifo}')
    print(deque_fifo.popleft())
    print(deque_fifo.popleft())
    print(deque_fifo.popleft())

    #5.queue.Queue - Parallel Computing
    queue_fifo = Queue()
    queue_fifo.put('eat')
    queue_fifo.put('sleep')
    queue_fifo.put('code')
    print(f'queue.Queue  queue FIFO: {queue_fifo}')
    print(queue_fifo.get()) # eat
    print(queue_fifo.get())# sleep
    print(queue_fifo.get())  # code
    # value = queue_fifo.get_nowait()  # Non-blocking
    # queue_fifo.get() # Blocks / waits forever ...

    #6.multiprocessing.Queue - Parallel Computing, Shared Jobs Queues
    ''' share data between processes. Can store and transfer any pickable object '''
    mpqueue_fifo = multiprocessing_Queue()
    mpqueue_fifo.put('eat')
    mpqueue_fifo.put('sleep')
    mpqueue_fifo.put('code')
    print(f'queue.Queue  queue FIFO: {mpqueue_fifo}')
    print(mpqueue_fifo.get()) # eat
    print(mpqueue_fifo.get()) # sleep
    print(mpqueue_fifo.get()) # code

    # mpqueue_fifo.get() # Blocks / waits forever ...

    #7 Priority Queues   List-based implementation O(nLogn)
    print(f'Priority Queue: List Based')

    pq = []
    pq.append((2,'code'))
    pq.append((1, 'eat'))
    pq.append((3, 'sleep'))

    pq.sort(reverse=True)

    while pq:
        next_item = pq.pop()
        print(next_item)


    #9  Priority quies  based on  Binary Heaps(heapq) O(LogN)
    print(f'Priority quies  based on  Binary Heaps(heapq) O(LogN), synchronized to locking semantics ')

    pq_main = PriorityQueue()
    pq_main.put((2,'code'))
    pq_main.put((1, 'eat'))
    pq_main.put((3, 'sleep'))

    while not pq_main.empty():
        next_item = pq_main.get()
        print(next_item)

    #8 Binary Heaps   List-based implementation O(LogN)
    print(f'Binary Heaps   List-based implementation O(LogN')

    hq = []
    heapq.heappush(hq, (2,'code'))
    heapq.heappush(hq, (1, 'eat'))
    heapq.heappush(hq, (3, 'sleep'))

    while hq:
        next_item = heapq.heappop(hq)
        print(next_item)