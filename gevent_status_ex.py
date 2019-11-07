import gevent

def win():
    return 'You win!'

def fail():
    #the exception will still be printed out to stderr
    raise Exception('You fail at failing.')

#another way to catch exception
# def process_exception(g):
#     try:
#         g.get()
#     except Exception as e:
#         print('This will never be reached')

winner = gevent.spawn(win)
loser = gevent.spawn(fail)

#another way to catch exception
#loser.link_exception(process_exception)

print(winner.started) # True
print(loser.started)  # True

# not properly working for some reason, have to check why
# Exceptions raised in the Greenlet, stay inside the Greenlet.
try:
    # g.get()
    gevent.joinall([winner, loser])
    # pass
except Exception as e:
    print('This will never be reached')


print(winner.value) # 'You win!'
print(loser.value)  # None

print(winner.ready()) # True
print(loser.ready())  # True

print(winner.successful()) # True
print(loser.successful())  # False

# The exception raised in fail, will not propagate outside the
# greenlet. A stack trace will be printed to stdout but it
# will not unwind the stack of the parent.

print(loser.exception)

# It is possible though to raise the exception again outside
# raise loser.exception
# or with
# loser.get()
