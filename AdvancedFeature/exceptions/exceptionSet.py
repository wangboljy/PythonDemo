class MyBaseExpection(Exception):
    def __init__(self, value):
        self.value = value
        Exception.__init__(self)

    def __str__(self):
        return repr(self.value)


class MyInputException(MyBaseExpection):
    def __init__(self, value):
        MyBaseExpection.__init__(self, value)


class MyDBException(MyBaseExpection):
    def __init__(self, value):
        MyBaseExpection.__init__(self, value)


if __name__ == '__main__':
    import traceback

    try:
        # raise MyDBException("connecting DB timeout")
        # raise MyInputException("input error")
        raise Exception("validation error")
    except MyDBException as e:
        print(e)
        traceback.print_exc()
    except MyInputException as e:
        print(e)
        traceback.print_exc()
    except Exception as e:
        print(">>> unknown exception\n" + str(e))
