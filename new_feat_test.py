# -*- coding:utf-8 -*-
__author__ = 'shichao'
import platform
import tensorflow as tf
import numpy as np
import time


def iterator_demo():
    '''
    python iterator demo
    :return:
    '''
    class numIter:  #
        def __init__(self, n):
            self.n = n

        def __iter__(self):
            self.x = -1
            return self

        if platform.python_version().startswith('2.'):
            def next(self):
                self.x += 1
                if self.x < self.n:
                    return self.x
                else:
                    raise StopIteration
        else:
            def __next__(self):  # Python 3.x version     Python 2.x version uses next()
                self.x += 1
                if self.x < self.n:
                    return self.x
                else:
                    raise StopIteration

    for i in numIter(5):
        print(i)
    print(isinstance(numIter(1),))
    print(isinstance(numIter,list))


def generator_demo():
    '''
    the generator demo
    :return:
    '''
    def numGen(n):  # generator
        try:
            x = 0
            while x < n:
                y = yield x
                print(y)
                x += 1
        except ValueError:
            yield 'error'
        finally:
            print('finally')



    num = numGen(5)
    print(num.next())
    print(num.next())
    print(num.send(999))
    num.close()
    # print(num.throw(ValueError))
    print(num.next())
    # print(num.next())


def bubblesort(array,length):
    '''
    the largest number will first down to the bottom, then the second largest, etc
    :param array:
    :param length:
    :return:
    '''
    sorted = False
    while not sorted:
        sorted = True
        for i in range(1,length):
            if array[i-1] > array[i]:
                [array[i-1],array[i]] = swap(array[i-1],array[i])
                sorted = False
                print(array)


def swap(a,b):
    tmp = a
    a = b
    b = tmp
    return [a,b]


def reverse_1(array,lo,hi):
    if lo<hi:
        array[lo],array[hi] = swap(array[lo],array[hi])
        reverse_1(array,lo+1,hi-1)
    return array

def reverse_2(array):
    pass

def power2(n):
    if n==0:
        return 1
    else:
        return power2(n>>1)**2<<1 if n&1 else power2(n>>1)**2

def power1(n):
    tmp = 1
    for i in range(n):
        tmp *= 2
    return tmp

def simple_decorater(f):
    def wrapper():
        print('enter')
        # f()
        int('exit')

    return wrapper

@ simple_decorater
def hello():
    print('hello')



def main():
    ##########
    # iterator and generator
    # iterator_demo()
    # generator_demo()

    #########
    # array operation
    # array = np.array([3,1,6,2,5,10,8,9,4,7])
    # # bubblesort(array,len(array))
    # array = reverse_1(array,0,len(array)-1)
    # print(array)
    #

    # #############
    # recursion vs for loop
    start = time.time()
    print('%E'%power2(1000))
    end = time.time()
    print('power2 elapsed time: {0}'.format(end-start))
    # print('power2 elapsed time: %E'%(end-start))

    start = time.time()
    print('%E'%power1(1000))
    end = time.time()
    # print('power1 elapsed time: %E'%(end-start))
    print('power1 elpased time: {0}'.format(end-start))


if __name__ == '__main__':
    # main()
    hello()