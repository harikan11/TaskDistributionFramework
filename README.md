# TaskDistributionFramework
Parallelization and distributed computing are the two major techniques to
optimise high CPU-intensive programming tasks. Unfortunately, most solutions
built presently are focused on using these optimizations in a single machine, by
utilising all the threads/CPU/GPU cores available on a single machine. Our goal
is to build a library on top of TCP sockets that provide an easy-to-use python
API to distribute tasks to multiple slave machines. Here's an implementation of an
algorithm to easily serialize/unserialize python functions, which will let us
easily transport them over TCP to other machines.
Future plans: To explore multiple strategies/algorithms to allocate tasks to
multiple machines and provide APIs to implement message passing between
processes.


Master.py file refers to the master node which is the centre of the whole system. It receives jobs and then
distributes them to slave nodes in the system. The master node also handles the
dynamic registration of clients and slaves. After a slave executes a function, it
sends back the result to the master, which in turn sends back the result to the
library.

Slave.py file refers to the slave node. The slaves are the actual workers of the system, which execute functions. They
receive serialized functions and arguments from the master node and then
deserialize and execute these functions. Then, it takes the result and passes it
back to the master node. The slave node also maintains an internal queue of
functions to execute. This means, if multiple jobs are assigned on the same
slave, it will pop off each job from the queue and execute them in an
asynchronous manner.

