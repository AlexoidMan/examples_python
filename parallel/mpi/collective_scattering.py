##  mpiexec -n 2 python3 collective_broadcast.py

from mpi4py import MPI
import random
comm = MPI.COMM_WORLD
rank = comm.rank #process ID


if rank == 0:
    # array = ['AAA', 'BBB', 'CCC', 'DDD']
    array = ['AAA', 'BBB']

else:
    array=None

data = comm.scatter(array, root=0)  #scatter array to all processes and to itself('AAA' = > process 0)

print("Process %d is working on %s  element" %(rank, data))


