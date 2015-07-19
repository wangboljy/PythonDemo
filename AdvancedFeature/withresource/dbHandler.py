#!/usr/bin/python


class DBHandler(object):
    def __init__(self, args):
        print(">>> init DBHandler...")
        print(args)
        self.__array = list(range(1, 10))

    def __enter__(self):
        print(">>> in __enter__ function")
        self.dbConn = self.getDBConn()
        print(">>> leaving __enter__")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(">>> in __exit__ function")
        self.closeDBConn()
        print(">>> leaving __exit__ function")

    def getDBConn(self):
        print(">>> in getDBConn...")
        return self.__array

    def closeDBConn(self):
        print(">>> in closeDBConn")
        print(">>> release connection")
        print(">>> in closeDBConn")

    def fetchOneRecord(self):
        i = 0
        while i < len(self.__array):
            yield self.__array[i]
            i += 1
        raise StopIteration


if __name__ == '__main__':
    with DBHandler('args asdf') as dbHandler:
        print(">>> counting")
        for record in dbHandler.fetchOneRecord():
            print(record, end=' ')
        print()
