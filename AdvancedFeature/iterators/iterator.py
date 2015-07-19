#!/usr/bin/python


class NotSupportException(Exception):
    def __init__(self):
        Exception.__init__(self)

    def __str__(self):
        return repr(self)


class Iterator(object):
    def __init__(self, data):
        if not isinstance(data, Array):
            raise NotSupportException
        self.__idx = 0
        self.__max = len(data)
        self.__data = data.getData()

    def __iter__(self):
        return self

    def __next__(self):
        if self.__idx >= self.__max:
            raise StopIteration
        idx = self.__idx
        self.__idx += 1
        return self.__data[idx]


class Array(object):
    def __init__(self, max):
        self.__array = list(range(0, max))
        self.__max = max
        self.__idx = 0

    def getIterator(self):
        return Iterator(self)

    def getData(self):
        return self.__array

    def __len__(self):
        return len(self.__array)

    # recommended
    def __iter__(self):
        return self

    def __next__(self):
        if self.__idx >= self.__max:
            raise StopIteration
        idx = self.__idx
        self.__idx += 1
        return self.__array[idx]


if __name__ == '__main__':
    array = Array(20)

    # not recommended
    it = array.getIterator()
    while True:
        try:
            print(it.__next__(), end=" ")
        except StopIteration:
            break
    print()

    # recommended
    for i in array:
        print(i, end=" ")
    print()
