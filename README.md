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
