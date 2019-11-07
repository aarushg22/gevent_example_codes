import gevent
import signal
from gevent.event import Event
from gevent.event import AsyncResult

'''
Illustrates the use of events
'''
evt = Event()
'''
An extension of events is AsyncResult, which allows you to send a value along with wakeup
'''
a = AsyncResult()


def setter():
    '''After 3 seconds, wake all threads waiting on the value of evt'''
    print('A: Hey wait for me, I have to do something')
    gevent.sleep(3)
    print("Ok, I'm done")
    #wakeup call without value
    evt.set()
    #wakeup call with value
    a.set('Everyone up?')


def waiter(choice):
    '''After 3 seconds the get call will unblock'''
    print("I'll wait for you")
    if choice:
        evt.wait()  # blocking
        print("It's about time")
    else:
        print(a.get()) #blocking

def main():
    #can be used to avoid "zombie processes", which will hold the program from shutting down
    gevent.signal(signal.SIGQUIT, gevent.kill)

    gevent.joinall([
        gevent.spawn(setter),
        gevent.spawn(waiter,1),
        gevent.spawn(waiter,1),
        gevent.spawn(waiter,1),
        gevent.spawn(waiter,0),
        gevent.spawn(waiter,0)
    ])

if __name__ == '__main__': main()
