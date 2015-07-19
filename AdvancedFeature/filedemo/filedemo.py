class FileDemo(object):
    def __init__(self, filename='filedemo.py'):
        self.__filename = filename

    def __enter__(self):
        self.file = open(self.__filename, mode='r')
        print(">>> file is ready")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

    def analyze(self):
        while True:
            line = self.file.readline()
            if not line:
                break
            print(line)

    def __call__(self, *args, **kwargs):
        self.analyze()


if __name__ == '__main__':
    with FileDemo() as fileDemo:
        fileDemo.analyze()

    # directly
    with open("filedemo.py", 'r') as file:
        for line in file.readlines():
            print(line)
