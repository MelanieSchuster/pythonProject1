#import sys

#print('Hello')
#a = None
#a.abv = 3575

#sys.stdout.write('OK')
#sys.stderr.write('Error')

#sys.exit(-1)

# run console on error code on the laptop then you get the error codes
# python interpreter gives us also an error code
# even without sys.exit would be an error message
# The python interpreter is communicating the error to us
# we see it in red and before the white hello because
# there are rwo output streams: one standard one and one error stream

#a = int(input('Provide a:'))
#b = 15
#c = b/a
#print('c: {}'.format(c))
#if c> 25:
#until here we don't provide any handling of the error code
# the code is not executed
# you have to be aware that without the exeption handling, when there is an error, the code stops in the middle and will not be executed
# when we don't want this: we want to react to a user input or we want to do to a certain point to a code

class MyError(Exception):
    pass

# it has to inherit from another exception
# most of them has the name error

a = int(input('Provide a:'))
b = 15
try:
    c = b/a
    print('c: {}'.format(c))
    if c> 10:
        raise MyError('c is greater than 10')
except ZeroDivisionError as de:
    print('I got zero devision: {}'.format(de))
except ArithmeticError as de:
    print('I got arithmetic error: {}'.format(de))
except MyError as me:
    print('MyError: {}'.format(me))
#except Exception as e:
#    print(type(e))
 #   print('Got Exception: {}'.format(e))
print('Finalizing my script')
# inheritance: the first suitable one will be taken
# errors may be of different type and depends on the level of inheritance
# the first one is checked and if its suitable it will be taken, if not, then the next one will be checked
# if there is an error that is not listed, the execution will be stopped
# how does except exception work?

a = int(input('Provide a:'))
b = 15
try:
    c = b/a
    print('c: {}'.format(c))
    if c> 10:
        aa = None
        aa.abv = 3252
except Exception as e:
    print(type(e))
    print('Got Exception: {}'.format(e))
except ZeroDivisionError as de:
    print('I got zero devision: {}'.format(de))
except ArithmeticError as de:
    print('I got arithmetic error: {}'.format(de))
print('Finalizing my script')

# what if I move Except Exception up to this place?
# except exception can catch all causes. It will catch all kind of exception
# very unsafe way to catch exceptions because you will catch everything without exceptions
# we have to be very careful when using this. Is should only be used when you don't absolutely want any error to be happen in that code
# can you thing about any cause of your computer where it is useful? there is a specific purpose:
# it makes sense when the browser crashes (then you can send the traceback (error) to the browser people)
# it is even more dangerous when it is the first one