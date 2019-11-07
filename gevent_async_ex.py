import time
import gevent
import random

start = time.time()
tic = lambda: 'at %1.3f seconds' % (time.time() - start)

def task(pid):
    """
    Some non-deterministic task, so wait for a random amount of time
    """
    #random sequence in output
    #because of a random time various tasks finish at different times
    gevent.sleep(random.randint(0,2)*0.001)

    #output is in the same order as it was spawned
    #Since all tasks take same time they all are started before the first one finishes
    #gevent.sleep(0.2)

    print('Task %s done' % pid)

def synchronous():
    """
    non-gevent way, each call is blocking
    """
    for i in range(1,10):
        task(i)


def asynchronous():
    """
    geven.spawn puts all the available calls in a array and assigns
    each call a greenlet, which then is executed asynchronously
    """
    threads = [gevent.spawn(task, i) for i in range(10)]
    #joinall blocks function until all threads are done
    gevent.joinall(threads)

print('Synchronous:')
synchronous()
print('Done Sync: %s', tic())

start = time.time()
print('Asynchronous:')
asynchronous()
print('Done Async: %s', tic())
