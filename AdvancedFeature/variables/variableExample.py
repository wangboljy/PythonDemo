def func(var, vardefault='default', *args, **kwargs):
    print("var: ", var)
    print("vardefault: ", vardefault)
    print("args:", args)
    print("kwargs:", kwargs)


# only strings are accepted as keyward in **kwargs
# call like this
func(12, "asdf", *(1, 'a', 2, 'b'), **{'us': 'american', 'ch': 'china', "one": 1})

# call like this
valist = (1, 'a', 2, 'b')
kvadict = {'us': 'american', 'ch': 'china', 'one': 1}
func(12, "asdf", *valist, **kvadict)

# call like this
func(12, "asdf", 1, 'a', 2, 'b', us='american', ch='china', one=1)


class Person:
    def __init__(self, name):
        self.name = name


func(12, "asdf", Person('a'), Person('b'), wb=Person('wb'), ljy=Person('ljy'))
