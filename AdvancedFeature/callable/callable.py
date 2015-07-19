class Callable:
    def __call__(self, *args, **kwargs):
        print(args)
        print(kwargs)


call = Callable()

call(1, 2, 3, *('a,', 'b'), **{'one': 1, 'two': 2})
