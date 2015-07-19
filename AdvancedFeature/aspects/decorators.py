from time import time

'''
Using decorator to do Aspect is not that perfect
1. two annotation decorated on one method will cause trouble for the later one
2. failure will happen when annotation without argument decorating methods in class

function based decorator works better.
'''


# demo for class-based decorator without parameters
class Profiling(object):
    def __init__(self, f):
        self.__f = f

    def __call__(self, *args, **kwargs):
        start = time()
        if not args and not kwargs:
            ret = self.__f()
        elif not kwargs:
            ret = self.__f(*args)
        elif not args:
            ret = self.__f(**kwargs)
        else:
            ret = self.__f(*args, **kwargs)

        end = time()
        print("cost %s in function %s" % (str(end - start), self.__f.__name__))
        return ret


# demo for class-based decorator with parameters
class Logging(object):
    def __init__(self, level='info', where='console'):
        self.__level = level
        self.__where = where

    def __call__(self, func):
        def log(*args, **kwargs):
            print(">>> %s: " % self.__level, args, kwargs)
            if not args and not kwargs:
                ret = func()
            elif not kwargs:
                ret = func(*args)
            elif not args:
                ret = func(**kwargs)
            else:
                ret = func(*args, **kwargs)
            print(">>> %s done" % self.__level)
            return ret

        # if you have other closures
        map = {'console': log, 'file': log}
        return map[self.__where]


def FuncMeteringNoArgs(func):
    def wrapper(*args, **kwargs):
        print(">>> entering metering")
        if not args and not kwargs:
            ret = func()
        elif not kwargs:
            ret = func(*args)
        elif not args:
            ret = func(**kwargs)
        else:
            ret = func(*args, **kwargs)
        print(">>> leaving metering")
        return ret

    return wrapper


def FuncMeteringWithArgs(arg1='info', arg2='console'):
    def wrapper(func):
        def wrapper_inner(*args, **kwargs):
            print(">>> %s: entering metering..." % arg1)
            if not args and not kwargs:
                ret = func()
            elif not kwargs:
                ret = func(*args)
            elif not args:
                ret = func(**kwargs)
            else:
                ret = func(*args, **kwargs)
            print(">>> %s: leaving metering..." % arg1)
            return ret

        map = {'console': wrapper_inner, 'file': wrapper_inner}
        return map[arg2]

    return wrapper


@FuncMeteringWithArgs()
# @FuncMeteringNoArgs
# @Profiling
# @Logging()
def sayhi():
    print("sayhi")


@FuncMeteringWithArgs(arg1='debug', arg2='file')
# @FuncMeteringNoArgs
# @Profiling
# @Logging(level='debug', where='file')
def sayhello(name, *a, **b):
    print(name, " hello", a, b)


class Test:
    def __init__(self):
        print(">>> Test init")

    @FuncMeteringWithArgs()
    # @FuncMeteringNoArgs
    # @Profiling # error happens
    # @Logging(level='debug')
    def test(self):
        print(">>> test in Test")

    @FuncMeteringWithArgs(arg1='debug', arg2='file')
    # @FuncMeteringNoArgs
    # @Profiling #error happens
    # @Logging()
    def test2(self, *arg):
        print(">>> test2 in Test", arg)


if __name__ == '__main__':
    sayhi()
    sayhello("wangboljy", 1, 2, 3, a="a", b="wb")

    tester = Test()
    tester.test()
    tester.test2(28)
