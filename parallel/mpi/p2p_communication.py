## mpiexec -n 4 python3 cores_based_example.py

from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.rank #process ID

print("The process %s is started"  %rank)

if rank == 0:
    msg = "This is my message"
    receiver = 1
    comm.send(msg, dest=receiver)
    print("Process 0 sent: %s" %msg + "to  %d" %receiver)

if rank == 1:
    source = 0
    msg = comm.recv(source)  #receive data from process 0
    print("Process 1 received is: %s" %msg + "from  %d" %source)

