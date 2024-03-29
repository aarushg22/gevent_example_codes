from gevent import sleep
from gevent.pool import Pool
from gevent.lock import BoundedSemaphore

sem = BoundedSemaphore(1)

def worker1(n):
    sem.acquire()
    print('Worker %i acquired semaphore' % n)
    sleep(0)
    sem.release()
    print('Worker %i released semaphore' % n)

def worker2(n):
    with sem:
        print('Worker %i acquired semaphore' % n)
        sleep(0)
    print('Worker %i released semaphore' % n)

pool = Pool()
pool.map(worker1, range(0,22))
pool.map(worker2, range(3,62))
