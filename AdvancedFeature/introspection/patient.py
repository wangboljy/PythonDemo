def patientFunc(arg, defaultarg='default', *args, **kwargs):
    def closure():
        pass

    return closure()


class PatientClass(object):
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name


patient_instance = PatientClass("not me")

if __name__ == '__main__':
    import inspect

    for name, data in inspect.getmembers(PatientClass):
        if name == '__builtins__':
            continue
        print("%s : " % name, repr(data))
    print("----------------")
    for name, data in inspect.getmembers(patientFunc):
        if name == '__builtins__':
            continue
        print("%s : " % name, repr(data))
    print("----------------")
    for name, data in inspect.getmembers(patient_instance):
        if name == '__builtins__':
            continue
        print("%s : " % name, repr(data))

    print("----------------")
    print(patientFunc.__code__.co_argcount)
    print(patientFunc.__code__.co_varnames)