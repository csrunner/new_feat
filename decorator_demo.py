import time
def timer(func):
    def f(*args,**kwargs):
        before = time.time()
        rv = func(*args,**kwargs)
        after = time.time()
        print('elapsed time :'.format(after-before))
        return rv
    return f

def add(x,y=10):
    return x+y
add = timer(add)

def sub(x,y=10):
    return x-y
sub = timer(sub)

print('add(10)', add(10))
print('sub(10)', sub(10))

@timer
def add_dec(x,y=20):
    return x+y

@timer
def sub_dec(x,y=0):
    return x-y

print('using decorator')
print('add(10)', add_dec(10))
print('sub(10)', sub_dec(10))
