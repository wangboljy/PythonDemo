#!/usr/bin/python


class Array(object):
    def __init__(self, max):
        self.__array = list(range(0, max))

    def values(self):
        i = 0
        while i < len(self.__array):
            yield self.__array[i]
            i += 1
        raise StopIteration

if __name__ == '__main__':
    for i in Array(20).values():
        print(i, end=" ")
    print()