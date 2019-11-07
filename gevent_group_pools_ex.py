import gevent
from gevent import getcurrent
from gevent.pool import Group

"""
groups can be used to manage and schedule tasks together
mirror the python multiprocessing by working as a parallel dispatcher
"""
group = Group()

def hello_from(n):
    print('Size of group %s' % len(group))
    print('Hello from Greenlet %s' % id(getcurrent()))

group.map(hello_from, range(3))


def intensive(n):
    gevent.sleep(3 - n)
    return 'task', n

print('Ordered')

ogroup = Group()
#imap send the iterable item by item preserving the order
for i in ogroup.imap(intensive, range(3)):
    print(i)

print('Unordered')

igroup = Group()
#Same as imap but doesn't care about order
for i in igroup.imap_unordered(intensive, range(3)):
    print(i)

"""
thread pool,  designed for handling dynamic numbers of
greenlets which need to be concurrency-limited
"""
from gevent.pool import Pool
from gevent import sleep

pool = Pool(2)

def hello_from(n):
    print('Size of pool %s' % len(pool))
    print('Hello from Greenlet %s' % id(getcurrent()))


pool.map(hello_from, range(3))
