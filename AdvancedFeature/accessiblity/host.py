#!/usr/bin/python


class Host(object):
    def __init__(self, ip, mac):
        self.__ip = ip
        self.__mac = mac

    def getIP(self):
        return self.__ip

    def getMAC(self):
        return self.__getMac()

    '''private function'''
    def __getMac(self):
        return self.__mac

    def __str__(self):
        return "host ip: %s\nhost mac: %s" % (self.__ip, self.__mac)

    def __eq__(self, other):
        if not isinstance(other, Host):
            return False
        return self.__mac == other.getMAC()


if __name__ == '__main__':
    host1 = Host("1.2.3.4", "asdf")
    host2 = Host("5.6.7.8", "fdsa")
    host3 = Host("9.8.7.6", "asdf")

    print(host1)

    print(host1 == host2)
    print(host1 == host3)

    print(">>> host1: %s, %s" % (host1.getIP(), host1.getMAC()))

    # will throw error
    # print(host1.__ip)
    # print(host1.__getMac())
