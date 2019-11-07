import gevent
from gevent import Timeout


def wait():
    gevent.sleep(2)

timer = Timeout(1).start()
thread1 = gevent.spawn(wait)

try:
    print('Thread 1 started')
    thread1.join(timeout=timer)
except Timeout:
    print('Thread 1 timed out')

# --

timer = Timeout.start_new(1)
thread2 = gevent.spawn(wait)

try:
    print('Thread 2 started')
    thread2.get(timeout=timer)
except Timeout:
    print('Thread 2 timed out')

# --

try:
    print('Thread 3 started')
    gevent.with_timeout(1, wait)
except Timeout:
    print('Thread 3 timed out')
